#!/usr/bin/python3
def best_score(a_dictionary):
    val = ''
    if a_dictionary:
        val = max(a_dictionary)
        return val
    else:
        return None
