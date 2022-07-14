from __future__ import annotations

import os
from pathlib import Path
import errno
import subprocess
import shutil
from ctypes import windll

def get_file_name_from_url(url: str) -> str:
    return url.split("/")[-1]

def ensure_install_path(install_path: str | Path):
    if isinstance(install_path, str):
        install_path = Path(install_path)
    install_path.mkdir(exist_ok=True, parents=True)
    return install_path

def check_if_elevated() -> bool:
    """Check if the current process has admin privileges.
    Returns
    -------
    bool
        True if elevated else false.
    """
    elevated = False
    # see https://stackoverflow.com/a/11995662/12858827
    if os.name == 'nt':
        # p = subprocess.run(["net", "session"], capture_output=True)
        # elevated = p.returncode == 0

        # See 
        # https://docs.microsoft.com/en-us/windows/win32/api/shlobj_core/nf-shlobj_core-isuseranadmin
        _shell32 = windll.shell32
        _is_admin = _shell32.IsUserAnAdmin()
        _is_admin.restype = (int, )
        try:
            return bool(_is_admin())
        except OSError:
            return False
    else:
        # linux: https://stackoverflow.com/a/2806932/12858827
        try:
            os.rename("/etc/foo", "/etc/bar")
            elevated = True
        except IOError as e:
            if e == errno.EPERM:
                elevated = False
    return elevated
