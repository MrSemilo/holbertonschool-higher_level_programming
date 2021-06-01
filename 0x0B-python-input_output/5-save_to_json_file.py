#!/usr/bin/python3
"""Writes an object to a file as json"""
import json


def save_to_json_file(my_obj, filename):
    """ditto the module description"""
    with open(filename, 'w') as file_:
        file_.write(json.dumps(my_obj))
