#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """ Returning a divided matrix"""
    new_list = []

    n = len(matrix[0])
    j = len(matrix[1])

    if n != j:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    for j in matrix:
        for a in j:
            if type(a) is not int and type(a) is not float:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    for i in range(len(matrix)):
        new_list.append(list(map(lambda x: round(x / div, 2), matrix[i])))

    return new_list
