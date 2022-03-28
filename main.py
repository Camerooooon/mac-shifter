#!/usr/bin/env python3
import argparse

from mac import reader as reader


def parser():
    parse = argparse.ArgumentParser()
    parse.add_argument("-o", "--option", help="Option")

    # Search Parsing
    subparsers = parse.add_subparsers(dest="search")
    subparser = subparsers.add_parser("search")
    subparser.add_argument("search", nargs="+", help="search for a mac address")
    return parse.parse_args()


if __name__ == "__main__":
    args = parser()

    if args.search:
        search = " ".join(args.search)
        print("Searching for: " + search)
        results = reader.get_search_results(search)
        index = 0
        for result in results:
            print("[" + str(index) + "] " + result[0])
            index += 1

        selection = input("Which one? #")
        selected_company = results[int(selection)][0]
        print(selected_company + " -> " + reader.get_mac(selected_company))

    if args.option:
        print("Option!")
