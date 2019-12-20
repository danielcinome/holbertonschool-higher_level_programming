#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        val = 0
        div = 0
        res = 0
        for i in range(len(my_list)):
            val = my_list[i][0] * my_list[i][1]
            div += my_list[i][1]
            res += val
        return res / div
    else:
        return
