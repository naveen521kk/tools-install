from pathlib import Path

from tools.utils.archives import extract_tar_file, extract_zip_file


def test_extract_tar_file(tmpdir):
    tmp_dir = Path(tmpdir)
    # download a tar file from the internet
    tar_file = Path(__file__).parent / "test_data" / "test_archive.tar.xz"
    assert tar_file.exists(), "tar file download exists"
    # test extract
    extract_tar_file(tar_file, tmp_dir)
    assert tmp_dir.exists(), "tmp_dir doesn't exists"
    assert (tmp_dir / 'test.txt').exists()

def test_extract_zip_file(tmpdir):
    tmp_dir = Path(tmpdir)
    # download a tar file from the internet
    zip_file = Path(__file__).parent / "test_data" / "test_archive.zip"
    assert zip_file.exists(), "tar file download exists"
    # test extract
    extract_zip_file(zip_file, tmp_dir)
    assert tmp_dir.exists(), "tmp_dir doesn't exists"
    assert (tmp_dir / 'test.txt').exists()
