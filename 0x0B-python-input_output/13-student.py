#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__.keys():
                    dic[i] = self.__dict__[i]
        return dic

    def reload_from_json(self, json):
        for i in json.keys():
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]
