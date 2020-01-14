#!/usr/bin/python3
"""
function that prints a square with the character #.
size is the size length of the square

"""


def print_square(size):
    """
    prints a square with the character #

    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size > 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end='')
        print("")
