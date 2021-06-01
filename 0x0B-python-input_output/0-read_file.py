#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, 'r') as file_:
        print(file_.read(), end="")
    file_.close()
