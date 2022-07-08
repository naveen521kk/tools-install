from tools.utils import cache
import os
from pathlib import Path

def test_get_cache_dir():
    assert 'tools' in os.fspath(cache.get_cache_dir()).lower()

def test_cache_round_trip(monkeypatch, tmpdir):
    tmpdir = Path(tmpdir)
    test_file = tmpdir / 'test.txt'
    with test_file.open('w') as f:
        f.write('test')
    def fake_cache_dir():
        return Path(tmpdir) / 'cache'
    monkeypatch.setattr(cache, 'get_cache_dir', fake_cache_dir)
    assert cache.get_cache_dir() == Path(tmpdir) / 'cache'
    assert cache.is_cached('test.txt', 'test') is None
    cache_file = cache.cache_file('test', test_file)
    assert cache.is_cached('test.txt', 'test') == cache_file
    assert cache.cache_file('test', test_file) is None
