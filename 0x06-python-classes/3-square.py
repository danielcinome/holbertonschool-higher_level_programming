#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) != int:
                raise TypeError
        except TypeError:
            print("size must be an integer", end='')
            raise TypeError
        except ValueError:
            print("size must be >= 0", end='')
            raise ValueError

    def area(self):
        return self.__size * self.__size
