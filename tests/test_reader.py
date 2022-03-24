from mac import reader
from mac import parser


def test_get_name_of_mac():
    parser.create_cache_file()
    assert reader.get_name_of_mac("28-BD-89") == "Google, Inc."
