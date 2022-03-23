from random import choice


class BaseMac:
    """BaseMac includes a template, that when self.fill is called, will
    overwrite each hash (#) with a random character from self.chars

    Create a new Mac by inheriting BaseMac and changing self.template and
    possibly self.chars. See TestMac for example.
    """

    template = "##:##:##:##:##:##"
    chars = "ABCDEFG12345"

    def __init__(self, dashes=False):
        self.dashes = dashes

    @property
    def mac(self) -> str:
        return self.fill()

    def fill(self) -> str:
        template_list = list(self.template)

        for i, character in enumerate(self.template):
            if character == "#":
                template_list[i] = choice(self.chars)

        filled_mac = "".join(template_list)

        if self.dashes:
            filled_mac = filled_mac.replace(":", "-")

        return filled_mac


class TestMac(BaseMac):
    """Using TestMac

    a = TestMac()
    print(a.mac)

    'AB:CD:GD:FA:1B:12'

    """

    template = "AB:CD:##:##:##:12"


class Google(BaseMac):
    template = "D8:EB:46:##:##:##"


class Apple(BaseMac):
    template = "60:8B:0E:##:##:##"
