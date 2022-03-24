from mac import reader


def test_get_name_of_mac():
    assert reader.get_name_of_mac("28-BD-89") == "Google, Inc."
