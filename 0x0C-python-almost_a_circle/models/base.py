#!/usr/bin/python3
"""
first class Base
"""
import json


class Base:
    """
     Class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return str("[]")
        else:
            return json.dumps(list_dictionaries)
