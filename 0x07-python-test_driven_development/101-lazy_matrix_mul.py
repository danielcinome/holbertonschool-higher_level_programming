#!/usr/bin/python3
"""
function that multiplies 2 matrices by using the module NumPy
Test cases should be the same as 100-matrix_mul
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices

    """

    return np.matmul(m_a, m_b)
