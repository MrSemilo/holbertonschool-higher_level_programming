#!/usr/bin/python3
"""Write a class MyList"""


class MyList(list):
    def __init__(self):
        """ def __init__"""
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
