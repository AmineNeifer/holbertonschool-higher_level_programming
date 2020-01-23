#!/usr/bin/python3
def pascal_triangle(n):
    """ function to make a pascal triangle.

        Args:
            n: number of rows we want of pascal triangle.

        Return: list fo lists of pascal rows."""
    l = []
    l2 = [0]
    l1 = [0, 1, 0]
    for i in range(n):
        j = 0
        while j < len(l1) - 1:
            l2 += [l1[j] + l1[j + 1]]
            j += 1
        l2 += [0]
        l.append(l1[1:-1])
        l1 = l2
        l2 = [0]
    return l
