#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        car = str[i]
        car = ord(car)
        if car in range(97, 122):
            car = car - 32
        print(chr(car), end='')
    print('')
