""" Utilities to extract tarballs and zip files. """
import logging
import tarfile
import zipfile
from pathlib import Path

log = logging.getLogger(__name__)


def extract_tar_file(file_path: Path, destination: Path) -> None:
    log.info(f"Extracting {file_path} to {destination}")
    # extract the tar file in file_path to destination
    with tarfile.open(file_path, "r") as tar_ref:
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar_ref, destination)


def extract_zip_file(file_path: Path, destination: Path) -> None:
    log.info(f"Extracting {file_path} to {destination}")
    # extract the zip file in file_path to destination
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(destination)
