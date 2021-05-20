#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """empty"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Returns"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Rectangle of __width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        """ Returns"""
        return self.__height
    
    @width.setter
    def height(self, value):
        """ Rectangle of __height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value