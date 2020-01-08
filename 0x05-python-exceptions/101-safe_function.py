#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = 0
    try:
        res = fct(*args)
        return res
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
