#!/usr/bin/python3
from sys import argv


save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

try:
    new_file = load("add_item.json")
    new_file += argv[1:]
except Exception:
    new_file = argv[1:]
save(new_file, "add_item.json")
