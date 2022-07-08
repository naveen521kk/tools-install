"""Read configuration file."""
import sys
from pathlib import Path

import tomli

from utils.misc import ensure_install_path

with open(Path(__file__).parent / 'config.toml', 'rb') as f:
    DATA = tomli.load(f)

INSTALL_PATH = Path(DATA['INSTALL_PATHS'][sys.platform]).expanduser()
ensure_install_path(INSTALL_PATH)
