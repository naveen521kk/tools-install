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
        tar_ref.extractall(destination)


def extract_zip_file(file_path: Path, destination: Path) -> None:
    log.info(f"Extracting {file_path} to {destination}")
    # extract the zip file in file_path to destination
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(destination)
