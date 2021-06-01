#!/usr/bin/python3
"""appends a string at the end of a text"""


def write_file(filename="", text=""):
    """write a file"""
    with open(filename, 'w') as fil:
        fil.write(text)
    return len(text)
