#!/usr/bin/python3
"""Print square with #"""


def print_square(size):
    """Edge cases for printing square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(0, size):
        for column in range(0, size):
            print("#", end="")
        print("")
    if size is 0:
        print("", end="")
