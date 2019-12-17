#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elements in matrix:
        for j in range(len(elements)):
            if j == len(elements) - 1:
                print("{:d}".format(elements[j]), end="")
            else:
                print("{:d}".format(elements[j]), end=" ")
        print()
