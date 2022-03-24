from mac import parser
from pathlib import Path

MAC_FILE = parser.get_mac_file()


def test_get_mac_file():
    mac_file = MAC_FILE

    assert len(mac_file) > 5000000
    assert "Google" in mac_file


def test_parse_mac_file():
    companies = parser.parse(MAC_FILE)
    assert companies["28-BD-89"] == "Google, Inc."


def test_create_cache_file():
    parser.create_cache_file()
    assert Path("data/macs_cache.csv").exists()


def test_open_cached_file():
    macs = parser.open_cached_file()
    assert macs["28-BD-89"] == "Google, Inc."


def test_remove_cache_file():
    parser.remove_cache_file(force=True)
    assert not Path("data/macs_cache.csv").exists()
