import hashlib
import logging
from pathlib import Path

_BLOCK_SIZE = 65536
log = logging.getLogger(__name__)


def hash_sha256(file_path: Path):
    """Returns the sha256 hash of the file."""
    log.info(f"Calculating sha256 hash of {file_path}...")
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        # loop till the end of the file, f
        chunk = f.read(_BLOCK_SIZE)
        while chunk != b"":
            # read only _BLOCK_SIZE bytes at a time
            h.update(chunk)
            chunk = f.read(_BLOCK_SIZE)
    _hash = h.hexdigest()
    log.debug(f"sha256 hash of {file_path}: {_hash}")
    return _hash


def verify_checksum(file_path: Path, checksum: str):
    """
    Verify the checksum of the file.
    """
    log.info(f"Verifying checksum of file {file_path}...")
    return hash_sha256(file_path) == checksum
