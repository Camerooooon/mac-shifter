"""Functions related to getting information based on mac address"""
from mac import parser as parser
from thefuzz import process


def get_name_of_mac(mac: str) -> str:
    pass


def get_mac(name: str) -> str:
    # We need to improve lookup times this is very slow!
    mac_file = parser.parse(parser.get_mac_file())
    for mac, company in mac_file.items():
        if company == name:
            return mac
    return "AA:AA:AA:AA:AA"


def get_search_results(query: str) -> []:
    to_search = parser.parse(parser.get_mac_file()).values()
    return process.extract(query, to_search, limit=5)
