from mac import gen


def test_mac():
    new_mac = gen.TestMac()
    mac = new_mac.mac

    assert mac[0] == "A"
    assert mac[1] == "B"

    assert mac[-1] == "2"
    assert mac[-2] == "1"


def test_new_mac():
    class NewMac(gen.BaseMac):
        template = "FF:11:##:##:##:##"

    new_mac = NewMac()
    mac = new_mac.mac

    assert mac[0] == mac[1] == "F"
    assert mac[3] == mac[4] == "1"
