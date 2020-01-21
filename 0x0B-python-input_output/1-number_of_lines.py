#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, 'r', encoding='utf-8') as my_file:
        n_lines = 0
        for i in my_file:
            n_lines += 1
        return n_lines
