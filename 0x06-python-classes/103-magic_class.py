#!/usr/bin/python3
import math


class MagicClass:
    '''ByCode'''
    def __init__(self, radius):
        if type(radius) != int and type(radius) != float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return self.__radius * math.pi * 2
