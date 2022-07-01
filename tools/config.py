"""Read configuration file."""
import tomli
from pathlib import Path
import sys
from utils.misc import ensure_install_path

with open(Path(__file__).parent / 'config.toml', 'rb') as f:
    DATA = tomli.load(f)

INSTALL_PATH = Path(DATA['INSTALL_PATHS'][sys.platform]).expanduser()
ensure_install_path(INSTALL_PATH)
