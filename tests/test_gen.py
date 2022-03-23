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
    assert mac[2] == mac[5] == ":"


def test_new_mac_dashes():
    class NewMac(gen.BaseMac):
        template = "FF:11:##:##:##:##"

    new_mac = NewMac(dashes=True)
    mac = new_mac.mac

    assert mac[0] == mac[1] == "F"
    assert mac[3] == mac[4] == "1"
    assert mac[2] == mac[5] == "-"


def test_mac_google():
    new_mac = gen.Google()
    a, b, c, _, _, _ = new_mac.mac.split(":")

    assert a == "D8"
    assert b == "EB"
    assert c == "46"


def test_mac_apple():
    new_mac = gen.Apple()
    a, b, c, _, _, _ = new_mac.mac.split(":")

    assert a == "60"
    assert b == "8B"
    assert c == "0E"
