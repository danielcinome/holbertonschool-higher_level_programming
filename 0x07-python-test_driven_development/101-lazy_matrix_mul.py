#!/bin/usr/python3
"""
function that multiplies 2 matrices by using the module NumPy
Test cases should be the same as 100-matrix_mul
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices

    """

    error1 = "m_a must be a list"
    error2 = "m_b must be a list"
    error3 = "m_a must be a list of lists"
    error4 = "m_b must be a list of lists"
    error5 = "m_a can't be empty"
    error6 = "m_b can't be empty"
    error7 = "m_a should contain only integers or floats"
    error8 = "m_b should contain only integers or floats"
    if type(m_a) is not(list):
        raise TypeError(erro1)
    if type(m_b) is not(list):
        raise TypeError(error2)
    for i in len(m_a):
        if type(m_a[i]) is not(list):
            raise TypeError(error3)
        if len(m_a) == 0 or len(m_a[i]) == 0:
            raise TypeError(error5)
        for j in len(m_a[i]):
            if type(m_a[i][j]) is not(int, float):
                raise TypeError(error7)
    for i in len(m_b):
        if type(m_b[i]) is not(list):
            raise TypeError(error4)
        if len(m_b) == 0 or len(m_b[i]) == 0:
            raise TypeError(error6)
        for j in len(m_b[i]):
            if type(m_b[i][j]) is not(int, float):
                raise TypeError(error8)
    return np.dot(m_a, m_b)
