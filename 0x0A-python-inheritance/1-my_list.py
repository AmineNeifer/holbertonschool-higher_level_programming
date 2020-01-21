#!/usr/bin/python3
""" one simple function that prints a list """


class MyList(list):
    """ prints a list sorted without changing the original list"""
    def print_sorted(self):
        l = self[:]
        l.sort()
        print(l)
