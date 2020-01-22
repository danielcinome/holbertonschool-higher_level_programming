#!/usr/bin/python3
import sys


save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

try:
    new_file = load("add_item.json")
except FileNotFoundError:
    new_file = []
for i in range(1, len(sys.argv)):
    new_file.append(sys.argv[i])
save(new_file, "add_item.json")
