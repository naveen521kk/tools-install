# Define that this installs a tool.
IS_TOOL = True

import os
import shutil
import sys
import tempfile
from pathlib import Path

import requests
from config import INSTALL_PATH

from utils.archives import extract_tar_file, extract_zip_file
from utils.checksums import hash_sha256
from utils.data import get_data
from utils.downloader import download
from utils.misc import get_file_name_from_url

TOOL_NAME = "starship"
DATA = get_data(TOOL_NAME)
DOWNLOAD_URLS = DATA["urls"]
GITHUB_REPO_API_URL = "https://api.github.com/repos/starship/starship"


def get_download_url():
    """Get the download url."""
    return DOWNLOAD_URLS[f"{sys.platform}_url"].format(
        version=DATA["version"],
    )


def get_latest() -> str:
    """Get the latest version of the tool.

    This is called by the updater script. This will get the latest
    version of the tool from Github and returns it as a string. This
    can be used by the updater in the future.

    Returns
    -------
    str:
        The latest version of the tool.
    """
    github_token = os.environ.get("GITHUB_TOKEN")
    headers = {}
    if github_token:
        headers.update({"Authorization": f"token {github_token}"})
    con = requests.get(GITHUB_REPO_API_URL + "/tags", headers=headers)
    con.raise_for_status()
    return con.json()[0]["name"].strip("v")


def install() -> int:
    """The main install function which will be called."""
    url = get_download_url()
    install_path = INSTALL_PATH
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        file = download(
            get_download_url(),
            tmpdir / get_file_name_from_url(url),
            TOOL_NAME,
        )
        if hash_sha256(file) != DOWNLOAD_URLS[f"{sys.platform}_hash"]:
            raise ValueError("Checksum mismatch. Please check if the issue is caused by cache, or update the checksum.")
        if file.name.endswith('.zip'):
            extract_zip_file(file, tmpdir)
            shutil.copytree(tmpdir / "starship", install_path)
        else:
            extract_tar_file(file, tmpdir)
            shutil.copy(tmpdir / "starship", install_path)
        print(f"{TOOL_NAME} installed successfully.")
    return 0

if __name__ == '__main__':
    sys.exit(install())
