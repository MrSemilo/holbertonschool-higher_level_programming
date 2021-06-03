#!/usr/bin/python3
"""Module MyList class"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initializes"""
        super().__init__()

    def print_sorted(self):
        """def print_sorted"""
        print(sorted(self))
