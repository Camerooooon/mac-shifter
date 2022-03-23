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

def parse(companies):
    lines = companies.split("\n")

    # Remove the first 4 lines because they contain junk information
    for i in range(4):
        lines.pop(0)

    cleaned_data = '\n'.join(lines)

    # Each company is a set of 5 lines seperated by a blank line. Split each company into their own list
    companies_list = cleaned_data.split("\r\n\r\n")

    to_return = {}

    # We only care about the first line since it contains the data we need
    for company in companies_list:
        company_lines = company.split("\n")
        mac_name = company_lines[0].split("   (hex)		")
        to_return[mac_name[0]] = mac_name[1]

    return to_return

