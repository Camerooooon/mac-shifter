import requests


def get_mac_file():
    mac_file = "https://standards-oui.ieee.org/oui/oui.txt"
    res = requests.get(mac_file)
    return res.text


def cache_file():
    pass


def open_cached_file():
    pass


def parser():
    pass
