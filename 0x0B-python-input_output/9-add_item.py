#!/usr/bin/python3
import sys
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
filename = "add_item.json"

try:
    l = load_from_json_file(filename)
except:
    with open(filename, 'w', encoding='utf_8') as f:
        f.write('')
        l = []
l += sys.argv[1:]
save_to_json_file(l, filename)
