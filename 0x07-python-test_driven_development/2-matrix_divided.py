#!/usr/bin/python3
"""
   Divide a matrix
   function that divides all elements of a matrix.
   Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
       matrix must be a list of lists of integers or floats
    """

    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    if type(matrix) != list:
        raise TypeError(error1)
    else:
        for i in range(len(matrix)):
            if type(matrix[i]) != list:
                raise TypeError(error1)
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                    raise TypeError(error1)
            if len(matrix[i]) == 0:
                raise TypeError(error1)
        for k in range(i):
            if len(matrix[k]) != len(matrix[i]):
                raise TypeError(error2)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda i: list(map(lambda j: round(j/div, 2), i)), matrix))
