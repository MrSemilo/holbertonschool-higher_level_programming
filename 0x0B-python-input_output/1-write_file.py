#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """write a file"""
    with open(filename, 'w') as fil:
        fil.write(text)
    return len(text)
