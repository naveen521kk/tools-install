"""Read configuration file."""
import tomli
from pathlib import Path

with open(Path(__file__).parent / 'config.toml', 'rb') as f:
    DATA = tomli.load(f)

INSTALL_PATHS = Path(DATA['INSTALL_PATHS'])
