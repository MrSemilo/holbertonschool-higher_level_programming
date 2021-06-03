#!/usr/bin/python3
"""class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """ def __init__"""
        super().__init__()

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """__str__"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
