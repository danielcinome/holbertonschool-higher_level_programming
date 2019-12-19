#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is str or roman_string:
        ant = roman[roman_string[0]]
        val = 0
        for i in roman_string:
            if roman[i] <= ant:
                val += roman[i]
                ant = roman[i]
            else:
                val = roman[i] - val
                ant = roman[i]
        return val
    else:
        return 0
