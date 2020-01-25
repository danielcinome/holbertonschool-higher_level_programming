#!/usr/bin/python3
""" class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = super().validation_type(value, "width")

    def __str__(self):
        return str("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))
