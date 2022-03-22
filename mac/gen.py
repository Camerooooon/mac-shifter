from random import choice


class BaseMac:
    """BaseMac includes a template, that when self.fill is called, will
    overwrite each hash (#) with a random character from self.chars

    Create a new Mac by inheriting BaseMac and changing self.template and
    possibly self.chars. See TestMac for example.
    """

    template = "##:##:##:##:##:##"
    chars = "ABCDEFG12345"

    @property
    def mac(self) -> str:
        return self.fill()

    def fill(self) -> str:
        new = list(self.template)

        for i, x in enumerate(self.template):
            if x == "#":
                new[i] = choice(self.chars)

        return "".join(new)


class TestMac(BaseMac):
    """Using TestMac

    a = TestMac()
    print(a.mac)

    'AB:CD:GD:FA:1B:12'

    """

    template = "AB:CD:##:##:##:12"
