#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        car = str[i]
        car = ord(car)
        if car in range(97, 123):
            car = car - 32
        print('{:}'.format(chr(car)), end='')
    print('')
