from mac import parser
from pathlib import Path

MAC_FILE = parser.get_mac_file()


def test_get_mac_file():
    mac_file = MAC_FILE

    assert len(mac_file) > 5000000
    assert "Google" in mac_file


def test_parse_mac_file():
    companies = parser.parse(MAC_FILE)

    name_indexs = [i for i, v in enumerate(companies["name"]) if v == "Google, Inc."]
    mac_index = companies["mac"].index("28-BD-89")
    assert mac_index in name_indexs


def test_create_cache_file():
    parser.create_cache_file()
    assert Path("data/macs_cache.csv").exists()


def test_open_cached_file():
    df = parser.open_cached_file()
    val = df["name"].where(df["mac"] == "28-BD-89")
    assert list(val) == 0


def test_remove_cache_file():
    parser.remove_cache_file(force=True)
    assert not Path("data/macs_cache.csv").exists()
