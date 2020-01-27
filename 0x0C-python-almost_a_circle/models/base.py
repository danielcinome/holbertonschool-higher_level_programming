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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        name = cls.__name__
        my_list = []
        if list_objs is not None:
            for i in list_objs:
                my_list.append(i.to_dictionary())
        with open(name + '.json', 'w') as json:
            json.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return list
        return json.loads(json_string)
