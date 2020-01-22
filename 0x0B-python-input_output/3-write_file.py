#!/usr/bin/python3
def write_file(filename="", text=""):
    """ opens a files, writes text into it, and return len(text)"""
    with open(filename, 'w', encoding='utf-8') as f:
        return(f.write(text))
