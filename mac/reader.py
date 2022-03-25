"""Functions related to getting information based on mac address"""
import parser as parser
from thefuzz import process

def get_name_of_mac(mac: str) -> str:
    pass

def get_search_results(query: str) -> []:
    to_search = parser.parse(parser.get_mac_file()).values()
    return process.extract(query, to_search, limit=5)
