#!/usr/bin/python3
def number_of_lines(filename=""):
    """ counts the number of lines"""
    lineNumb = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            lineNumb += 1
    return lineNumb
