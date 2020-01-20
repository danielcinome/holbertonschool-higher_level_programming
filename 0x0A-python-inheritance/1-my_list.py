#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        n_list = list.copy(self)
        n_list.sort()
        print(n_list)
