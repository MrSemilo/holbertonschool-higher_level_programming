#!/usr/bin/python3
""" moduel of add_atribute """


def add_attribute(a_class, key, value):
    """adds"""
    if hasattr(a_class, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(a_class, key, value)
