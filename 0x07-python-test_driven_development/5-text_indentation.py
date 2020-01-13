#!/usr/bin/python3
""" contains a function that manages a text indentation."""


def text_indentation(text):
    """Args: text.

       Raises: TypeError: when text is not an int.
    """
    i = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print()
            print()
            if text[i+1] == " ":
                i += 1
        i += 1
