# Copyright (c) 2022, Naveen M K. All rights reserved.

# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
This is the main entry point for installing the tools.

There are some dependencies that needs to be installed before running
this script. They can be installed using `requirements.txt` file found
in the root directory. Alternatively, poetry can be used:

    poetry install

Adding a new installing script should be done in `tools/` directory.
It's expected that each script in `tools/` directory will have a
`install()` function that will be called for every script.
Also, the file should contain a variable called `IS_TOOL` defined
to `True`, only then this script will assume that the script is a tool.
Mostly no code should be run when importing the file, instead should
be in the `install()` function.
"""
import importlib
import logging
import os
import sys
import argparse
from pathlib import Path
import traceback

from rich import print
from rich.logging import RichHandler

LOG_FORMAT = "%(message)s"
TOOLS_DIR = Path(__file__).parent / "tools"

# Add TOOLS_DIR to sys.path
sys.path.append(os.fspath(TOOLS_DIR))


def main(**kwargs):
    """Main entry function that can be called."""
    if kwargs.get("debug"):
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    _logging_handlers = [RichHandler(rich_tracebacks=True)]
    if not kwargs.get("no_log_to_file"):
        _logging_handlers.append(logging.FileHandler("tools.log", encoding="utf-8"))
    logging.basicConfig(
        level=log_level,
        format=LOG_FORMAT,
        handlers=_logging_handlers,
    )
    for tool in TOOLS_DIR.iterdir():
        if tool.name == "config.py":
            # skip config.py
            continue
        ret = 1
        if tool.is_file() and tool.name.endswith(".py"):
            tool_name = tool.name[:-3]
            module = importlib.import_module(tool_name)
            if hasattr(module, "IS_TOOL") and module.IS_TOOL:
                try:
                    ret = module.install()
                except Exception as e:
                    traceback.print_exc()
                    print(e)
                    ret = 1
                if ret == 1:
                    print(f"{tool_name} had error while installing.")
                    print("Please check the logs for more information.")
                else:
                    print(f"{tool_name} installed successfully.")
            else:
                print(f"{tool} isn't a tool. Skipping...")
    print("[green]All tools installed successfully.[/green]")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Install tools from `tools/`.")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode.")
    parser.add_argument("--no-log-to-file", action="store_true", help="Don't log to file.")
    sys.exit(main(**vars(parser.parse_args())))
