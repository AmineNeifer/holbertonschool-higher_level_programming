#!/usr/bin/python3
""" contains a function to check for class """


def is_kind_of_class(obj, a_class):
    """ Args:
            obj: an instance.
            a_class: any class.
        Returns:
            True if instance's type is a_class or some subclass
derived for a_class
            False otherwise"""
    return isinstance(obj, a_class)
