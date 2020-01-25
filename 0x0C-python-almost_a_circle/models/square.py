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

    def update(self, *args, **kwargs):
        if len(args) != 0 and args is not None:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.__size = self.validation_type(args[1], "width")
            if len(args) == 3:
                self.x = self.validation_type(args[2], "x")
            if len(args) == 4:
                self.y = self.validation_x_y(args[3], "y")
        else:
            for name, value in kwargs.items():
                if name == "id":
                    self.id = value
                if name == "size":
                    self.__size = self.validation_type(value, "width")
                if name == "x":
                    self.x = self.validation_type(value, "x")
                if name == "y":
                    self.y = self.validation_x_y(value, "y")

    def __str__(self):
        return str("[Square] ({}) {}/{} - {}".format(
            self.id, self.__x, self.__y, self.__size))

    def to_dictionary(self):
        return {'id': self.id, 'size': self.__size,
                'x': self.__x, 'y': self.__y}
