#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = ''
        val = max(a_dictionary, key=a_dictionary.get)
        return val
    else:
        return None
