# Define that this installs a tool.
IS_TOOL = True

import logging
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from utils.downloader import download
from utils.misc import check_if_elevated, get_file_name_from_url

TOOL_NAME = "chocolatey"
log = logging.getLogger(__name__)
INSTALLER_SCRIPT_URL = "https://community.chocolatey.org/install.ps1"


def install() -> int:
    """The main install function which will be called."""
    # check we are on windows
    if not sys.platform.startswith("win32"):
        # choco is windows only software
        log.info(f"Skipping install of {TOOL_NAME} as not on windows")
        return 0
    if not check_if_elevated():
        raise RuntimeError("This script must be run as admin")
    # check if powershell is there
    if not shutil.which("powershell"):
        raise RuntimeError("powershell is not installed")
    # check if chocolatey is there
    if shutil.which("choco"):
        log.info("Chocolatey is already installed. Skipping...")
        return 0
    # download chocolatey install script
    log.info(f"Downloading {TOOL_NAME} installer script")
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        installer_loc = tmpdir / get_file_name_from_url(INSTALLER_SCRIPT_URL)
        download(
            INSTALLER_SCRIPT_URL,
            installer_loc,
            TOOL_NAME,
        )
        # checking the checksum of the installer script is useless
        # as it is a powershell script and not a binary
        # so we just run it
        log.info(f"Installing {TOOL_NAME}")
        subprocess.run(
            ["powershell", os.fspath(installer_loc)],
        )
        log.info("Successfully installed chocolatey.")
    return 0


if __name__ == "__main__":
    sys.exit(install())
