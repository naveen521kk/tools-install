import logging
import os
import shutil
from pathlib import Path

import requests
from rich.progress import Progress

from . import cache
log = logging.getLogger(__name__)

def _download_from_url(url: str, file_path: Path) -> bool:
    log.info(f"Downloading {url} to {file_path}")
    max_value = 100
    with Progress(transient=True) as progress:
        with requests.get(url, stream=True) as r:
            if 'content-length' in r.headers:
                max_value = int(r.headers['content-length'])
            task = progress.add_task("Downloading file.", total=max_value)
            r.raise_for_status()
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    f.write(chunk)
                    try:
                        progress.update(task, advance=8192)
                    except ValueError:
                        pass
    return True


def download(url: str, file_path: Path, tool_name: str = None) -> Path:
    """Download a file. Check if the file exists in the
    cache first when :param:`tool_name` is provided. If the file
    is not found in the cache, then download the file and cache it.

    Parameters
    ----------
    url : str
        The url to download from.
    file_path : Path
        The path to store the file.
    tool_name : str, optional
        The name of the tool downloading, by default None. If this is None,
        caching is disabled.

    Returns
    -------
    Path:
        The path of the file downloaded.
    """
    if tool_name is not None:
        if cache_path := cache.is_cached(file_path.name, tool_name):
            shutil.copyfile(os.fspath(cache_path), os.fspath(file_path))
            return file_path
    assert _download_from_url(url, file_path), "Something failed?"
    if tool_name:
        cache.cache_file(tool_name, file_path)
    return file_path
