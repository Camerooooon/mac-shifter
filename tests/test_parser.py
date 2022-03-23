from mac import parser


def test_get_mac_file():
    mac_file = parser.get_mac_file()

    assert len(mac_file) > 5000000
    assert "Google" in mac_file


def test_parse_mac_file():
    companies = parser.parse(parser.get_mac_file())
    assert companies["28-BD-89"] == "Google, Inc."
