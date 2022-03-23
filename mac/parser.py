import requests
from typing import Dict, List
from os import remove
import json


def get_mac_file() -> str:
    mac_file = "https://standards-oui.ieee.org/oui/oui.txt"
    res = requests.get(mac_file)
    return res.text


def create_cache_file():
    macs = parse(get_mac_file())
    with open("data/macs_cache.csv", "w") as file:
        json.dump(macs, file)


def open_cached_file():
    with open("data/macs_cache.csv") as file:
        return json.load(file)


def remove_cache_file(force=False):
    path = "data/macs_cache.csv"

    if force:
        remove(path)
    else:
        res = input(f"Are you sure you wan't to remove {path}? [y/N]: ")
        low = res.lower()
        if low == "y" or low == "yes":
            remove(path)


def parse(companies) -> Dict[str, List[str]]:
    lines = companies.split("\n")

    # Remove the first 4 lines because they contain junk information
    for _ in range(4):
        lines.pop(0)

    cleaned_data = "\n".join(lines)

    # Each company is a set of 5 lines seperated by a blank line. Split each company into their own list
    companies_list = cleaned_data.split("\r\n\r\n")

    to_return = {}

    # We only care about the first line since it contains the data we need
    for company in companies_list:
        company_lines = company.split("\n")
        mac, name = company_lines[0].split("   (hex)		")
        to_return[mac] = name.rstrip("\r")

    return to_return
