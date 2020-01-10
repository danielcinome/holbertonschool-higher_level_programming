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
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size
