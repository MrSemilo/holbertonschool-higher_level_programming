#!/usr/bin/python3
"""appends a string at the end of a text"""


def append_write(filename="", text=""):
    """write a file"""
    with open(filename, 'a') as fil:
        fil.write(text)
    return len(text)
