#!/usr/bin/python3
""" contains a single function that returns list """


def lookup(obj):
    """ Args: obj: object

        Returns: list of available attributes and mothods of obj """

    return dir(obj)
