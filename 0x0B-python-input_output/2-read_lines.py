#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as my_file:
        n_lines = 0
        for i in my_file:
            n_lines += 1

        if nb_lines <= 0 or nb_lines >= n_lines:
            my_file.seek(0)
            print(my_file.read())
        else:
            my_file.seek(0)
            for j in range(nb_lines):
                line = my_file.readline()
                print(line)
