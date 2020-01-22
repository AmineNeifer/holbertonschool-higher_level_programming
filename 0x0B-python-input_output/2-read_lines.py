#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ prints nb_lines lines

        Args:
            filename
            nb_lines: number of lines"""
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            i = 0
            for line in f:
                i += 1
                print(line, end='')
                if i == nb_lines:
                    break
