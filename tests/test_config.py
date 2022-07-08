import os
from tools.config import DATA, INSTALL_PATH

def test_config_data():
    assert DATA["INSTALL_PATHS"]["linux"] == "~/.local/bin"
    assert DATA["INSTALL_PATHS"]["win32"] == "C:\\tools\\bin"

def test_install_path():
    assert INSTALL_PATH.exists()
    assert '~' not in os.fspath(INSTALL_PATH)
