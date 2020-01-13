#!/usr/bin/python3
"""matrix_divided is a function in which we enter two variables, matrix and div
   and it divides every number in it by div"""


def matrix_divided(matrix, div):
    """Args: matrix: list type
             div: integer/float type
       Returns:
             a new matrix with results of dividing
             the first matrix numbers by div"""
    new_matrix = []
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
        of integers/floats")
    for items in matrix:
        if not isinstance(items, list):
            raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")
        for i in items:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    test = True
    for items in matrix:
        if len(items) != len(matrix[0]):
            test = False
    if test is False:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][j] / div, 2))
    return new_matrix
