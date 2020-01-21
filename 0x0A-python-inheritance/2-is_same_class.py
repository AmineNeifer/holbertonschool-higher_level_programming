#!/usr/bin/python3
""" module with one function determines if an object
    is from a class given or not"""


def is_same_class(obj, a_class):
    """ Args:
            obj: any object from anytype
            a_class: like int or str ...

        Returns:
            True if obj is from type : a_class
            False otherwise"""
    return(type(obj) == a_class)
