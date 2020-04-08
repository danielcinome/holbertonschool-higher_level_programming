#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """
def find_peak(list_of_integers):
    if len(list_of_integers) > 0:
        val = max(list_of_integers)
        return val
    return None
