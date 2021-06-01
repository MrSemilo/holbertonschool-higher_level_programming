#!/usr/bin/python3


def read_file(filename=""):
    """read file and print"""
    with open(filename, 'r') as file_:
        print(file_.read(), end="")
    file_.close()
