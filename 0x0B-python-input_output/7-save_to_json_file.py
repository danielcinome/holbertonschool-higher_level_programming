#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='UTF-8') as file_json:
        txt = json.JSONEncoder().encode(my_obj)
        file_json.write(str(txt))
