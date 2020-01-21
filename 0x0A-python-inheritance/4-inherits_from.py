#!/usr/bin/python3
""" contain function that check if a class is subclass of another or not"""


def inherits_from(obj, a_class):
    """ Args:
            obj: any object from anytype
            a_class: like int or str ...

        Returns:
            True if obj is subclass derivded from a_class
            False otherwise"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
