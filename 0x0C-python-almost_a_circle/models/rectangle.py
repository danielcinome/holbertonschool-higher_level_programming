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
        return value

    @staticmethod
    def validation_type(value, name):
        """ validation type of data
            int for width and height
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be > 0")
        return value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = self.validation_type(value, "width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = self.validation_type(value, "height")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = self.validation_x_y(value, "x")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = self.validation_x_y(value, "y")

    def area(self):
        """ Return Area """
        return self.__width * self.__height

    def display(self):
        """ Print Rectangle """
        for k in range(0, self.__y):
            print('')

        for i in range(0, self.__height):
            for l in range(0, self.__x):
                print(' ', end='')
            for j in range(0, self.__width):
                print("#", end='')
            print('')

    def __str__(self):
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        if len(args) != 0 and args is not None:
            if len(args) == 1:
                super().__init__(args[0])
            if len(args) == 2:
                self.__width = self.validation_type(args[1], "width")
            if len(args) == 3:
                self.__height = self.validation_type(args[2], "height")
            if len(args) == 4:
                self.__x = self.validation_x_y(args[3], "x")
            if len(args) == 5:
                self.__y = self.validation_x_y(args[4], "y")
        else:
            for name, value in kwargs.items():
                if name == "id":
                    super().__init__(value)
                if name == "width":
                    self.__width = self.validation_type(value, "width")
                if name == "height":
                    self.__height = self.validation_type(value, "height")
                if name == "x":
                    self.__x = self.validation_x_y(value, "x")
                if name == "y":
                    self.__y = self.validation_x_y(value, "y")

    def to_dictionary(self):
        return {'id': self.id, 'widht': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
