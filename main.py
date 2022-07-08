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
import os
import sys
from pathlib import Path

from rich import print

TOOLS_DIR = Path(__file__).parent / "tools"

# Add TOOLS_DIR to sys.path
sys.path.append(os.fspath(TOOLS_DIR))


def main():
    """Main entry function that can be called."""
    for tool in TOOLS_DIR.iterdir():
        if tool.is_file() and tool.name.endswith(".py"):
            tool_name = tool.name[:-3]
            module = importlib.import_module(tool_name)
            if hasattr(module, "IS_TOOL") and module.IS_TOOL:
                module.install()
            else:
                print(f"{tool} isn't a tool. Skipping...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
