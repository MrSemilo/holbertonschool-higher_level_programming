#!/usr/bin/python3
"""File: 3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """def is_kind_of_class(obj, a_class):"""
    if type(obj) is a_class or isinstance(obj, a_class):
        return True

    else:
        return False
