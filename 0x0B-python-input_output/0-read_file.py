#!/usr/bin/python3
""" contains a function that reads a file"""


def read_file(filename=""):
    """ Args: filname. """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
