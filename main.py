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

"""
import sys


def main():
    """
    main entry function that can be called.
    """


if __name__ == "__main__":
    sys.exit(main())
