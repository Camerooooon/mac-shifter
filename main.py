#!/usr/bin/env python3
import argparse


def parser():
    parse = argparse.ArgumentParser()
    parse.add_argument("-o", "--option", help="Option")
    return parse.parse_args()


if __name__ == "__main__":
    args = parser()

    print("mac-shifter")

    if args.option:
        print("Option!")
