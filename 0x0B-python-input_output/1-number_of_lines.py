#!/usr/bin/python3


def number_of_lines(filename=""):
    with open('my_file_0.txt', 'r') as my_file:
        n_lines = 0
        for i in my_file:
            n_lines += 1
        return n_lines
