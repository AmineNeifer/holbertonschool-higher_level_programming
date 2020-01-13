#!/usr/bin/python3
""" contains only one function that prints squares out of hashes. """
def print_square(size):
    """Args:
        size: integer type.

       Raises:
        TypeError: when size is a float and less than zero or size isn't int.
        ValueError when size is less than zero.
    """
    if type(size) is float and (size < 0.0):
        raise TypeError("size must be an integer")
    elif type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
