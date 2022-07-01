import hashlib
from pathlib import Path

_BLOCK_SIZE = 65536

def hash_sha256(file_path: Path):
    """
    Returns the sha256 hash of the file.
    """
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        # loop till the end of the file, f
        chunk = f.read(_BLOCK_SIZE)
        while chunk != b'':
           # read only _BLOCK_SIZE bytes at a time
           h.update(chunk)
           chunk = f.read(_BLOCK_SIZE)
    return h.hexdigest()

def verify_checksum(file_path: Path, checksum: str):
    """
    Verify the checksum of the file.
    """
    return hash_sha256(file_path) == checksum
