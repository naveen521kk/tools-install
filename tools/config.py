"""Read configuration file."""
import logging
import sys
from pathlib import Path

import tomli

from utils.misc import ensure_install_path

log = logging.getLogger(__name__)

log.info("Reading configuration file...")
with open(Path(__file__).parent / "config.toml", "rb") as f:
    DATA = tomli.load(f)
log.debug(
    f"Configuration file contents: {DATA}",
)
INSTALL_PATH = Path(DATA["INSTALL_PATHS"][sys.platform]).expanduser()
ensure_install_path(INSTALL_PATH)
log.info(
    f"Installation Path: {INSTALL_PATH}",
)
