#!/usr/bin/python3


def read_file(filename=""):
    with open('my_file_0.txt', 'r') as my_file:
        print(my_file.read())
