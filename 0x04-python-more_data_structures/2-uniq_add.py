#!/usr/bin/python3
def uniq_add(my_list=[]):
    val = 0
    new_list = list(set(my_list))
    for i in range(len(new_list)):
        val += new_list[i]
    return val
