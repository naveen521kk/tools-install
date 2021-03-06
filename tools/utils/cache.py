from __future__ import annotations

import logging
import shutil
from pathlib import Path

from platformdirs import PlatformDirs

_dirs = PlatformDirs("ToolsInstall", "Naveen")
log = logging.getLogger(__name__)


def get_cache_dir() -> Path:
    return Path(_dirs.user_cache_dir)


def is_cached(file_name: str, tool_name: str) -> None | Path:
    """Check if the file present in cache.

    Parameters
    ----------
    file_name : str
        The name of the file.
    tool_name: str
        The name of the tool requesting the cache.

    Returns
    -------
    None | Path
        If the file is cached the path to the file is returned, else
        None is returned.
    """
    log.info(f"Checking if '{file_name}' is cached...")
    file = get_cache_dir() / tool_name / file_name
    if file.exists():
        log.info(f"'{file_name}' is already cached.")
        return file
    log.info(f"'{file_name}' is not cached.")
    return


def cache_file(tool_name: str, file_path: Path) -> Path:
    """Cache the file.

    Parameters
    ----------
    tool_name : str
        The name of the tool.
    file_path : Path
        The path of the file.
    """
    if is_cached(file_path.name, tool_name):
        return
    log.info(f"Caching {file_path}...")
    dir = get_cache_dir() / tool_name
    dir.mkdir(exist_ok=True, parents=True)
    cache_file = dir / file_path.name
    shutil.copyfile(file_path, cache_file)
    return cache_file
