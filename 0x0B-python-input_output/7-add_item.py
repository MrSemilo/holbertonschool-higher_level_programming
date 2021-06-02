#!/usr/bin/python3
""" Add items in a list """

from os import path
from sys import argv
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":

    list_new = []

    """ if file exists """
    if path.isfile("add_item.json"):
        list_new = load("add_item.json")

    list_new.extend(argv[1:])

    save(list_new, "add_item.json")
