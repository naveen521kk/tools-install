from __future__ import annotations
from pathlib import Path

def get_file_name_from_url(url: str) -> str:
    return url.split("/")[-1]

def ensure_install_path(install_path: str | Path):
    if isinstance(install_path, str):
        install_path = Path(install_path)
    install_path.mkdir(exist_ok=True, parents=True)
    return install_path