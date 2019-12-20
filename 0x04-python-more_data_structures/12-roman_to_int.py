#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string == "":
        return 0
    else:
        r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ant = r[roman_string[0]]
        val = 0
        for i in roman_string:
            if r[i] <= ant:
                val += r[i]
                ant = r[i]
            else:
                val = r[i] - val
                ant = r[i]
        return val
