#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string:
        val = 0
        for i in range(len(roman_string)):
            if val < roman[roman_string[i]]:
                val += roman[roman_string[i]]
            if val > roman[roman_string[i]]:
                val += roman[roman_string[i]]
        return val
    else:
        return 0
