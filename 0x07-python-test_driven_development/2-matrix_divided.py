#!/usr/bin/python3
"""This module supplies one function, matrix_divided(matrix, div)"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        for x in row:
            if not isinstance(x, float) and not isinstance(x, int):
                raise TypeError(type_err)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(
        lambda row: list(map(
            lambda x: round(x / div, 2), row)), matrix))
    return new_matrix
