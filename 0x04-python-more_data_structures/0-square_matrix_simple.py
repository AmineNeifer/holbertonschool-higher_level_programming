#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    maty = []
    for x in matrix:
        maty.append(list(map(lambda i: i ** 2, x)))
    return (maty)
