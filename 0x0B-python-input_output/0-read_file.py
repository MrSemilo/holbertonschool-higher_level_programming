#!/usr/bin/python3
"""reads a file and prints"""


def read_file(filename=""):
    """read file and print"""
    with open(filename, 'r') as file_:
        print(file_.read(), end="")
    file_.close()
