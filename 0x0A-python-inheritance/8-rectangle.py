#!/usr/bin/python3
"""empty class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class"""

    def __init__(self, width, height):
        """ def __init__"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
