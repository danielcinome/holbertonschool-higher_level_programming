#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as ptr_error:
        print("Exception:{}".format(ptr_error), file=sys.stderr)
        return False
