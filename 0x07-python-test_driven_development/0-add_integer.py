#!/usr/bin/python3
""" add_integer is a function that takes
    two arguments a and b that must be integer or float
    and calculates their sum"""


def add_integer(a, b=98):
    """Args: a: int or float
             b: int or float
       Returns: the sum of a and b"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
