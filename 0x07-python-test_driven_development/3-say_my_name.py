#!/usr/bin/python3
""" say_my_name is a function that takes two strings, first name and last name
    and outputs a message of greeting"""


def say_my_name(first_name, last_name=""):
    """Args: first_name: str type.
             last_name: str type.
       Returns: Nothing"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
