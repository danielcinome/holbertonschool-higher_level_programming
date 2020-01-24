#!/usr/bin/python3
""" class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def validation_x_y(value, name):
        """ validation type of data
            int for x and y
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value < 0:
            raise ValueError(name + " must be >= 0")

    @staticmethod
    def validation_type(value, name):
        """ validation type of data
            int for width and height
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be > 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validation_type(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validation_type(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validation_x_y(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validation_x_y(value, "y")
        self.__y = value

    def area(self):
        """ Return Area """
        return self.__width * self.__height

    def display(self):
        """ Print REctangle """
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print("#", end='')
            print('')

    def __str__(self):
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))
