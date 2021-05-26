#!/usr/bin/python3
"""Function to print two names"""


def say_my_name(first_name, last_name=""):
    """Edge cases for trying to print names
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
