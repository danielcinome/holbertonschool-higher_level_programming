#!/usr/bin/python3
"""function that adds 2 integers.
   Returns an integer: the addition of a and b
   a and b must be integers or floats, otherwise raise a TypeError
   exception with the message a must be an integer or b must be an integer
"""


def add_integer(a, b=98):
    """
       a and b must be integers or floats
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
