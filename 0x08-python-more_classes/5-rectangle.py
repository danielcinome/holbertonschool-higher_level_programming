#!/usr/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            rect = ''
            return rect
        else:
            rect = (('#' * self.__width + '\n') * (self.__height - 1))
            return (rect + ('#' * self.__width))

    def __repr__(self):
        new = "Rectangle("+str(self.__width)+", "+str(self.__height)+")"
        return new

    def __del__(self):
        print("Bye rectangle...")

if __name__ == "__main__":
    x = Rectangule()
    del x
