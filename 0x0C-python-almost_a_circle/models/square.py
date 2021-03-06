#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter size
        """
        self.width = super().validation_type(value, "width")

    def update(self, *args, **kwargs):
        """
        Update data
        """
        if len(args) != 0 and args is not None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = self.validation_type(args[1], "width")
            if len(args) >= 3:
                self.x = self.validation_type(args[2], "x")
            if len(args) >= 4:
                self.y = self.validation_x_y(args[3], "y")
        else:
            for name, value in kwargs.items():
                if name == "id":
                    self.id = value
                if name == "size":
                    self.size = self.validation_type(value, "width")
                if name == "x":
                    self.x = self.validation_type(value, "x")
                if name == "y":
                    self.y = self.validation_x_y(value, "y")

    def __str__(self):
        """
        pritn this format
        """
        return str("[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size))

    def to_dictionary(self):
        """
        Dictionary
        """
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
