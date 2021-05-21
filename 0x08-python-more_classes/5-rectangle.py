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

    @height.setter
    def height(self, value):
        """ Rectangle of __height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the rectangle area"""
        return (self.height * self.width)

    def perimeter(self):
        """ Returns the rectangle perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (2 * (self.width + self.height))

    def __str__(self):
        """ Print the rectangle with the character #"""
        s = ""
        if self.__height == 0 or self.__width == 0:
            return s
        for i in range(0, self.__height):
            if i < self.__height - 1:
                s = s + ("#" * self.__width + "\n")
            else:
                s = s + ("#" * self.__width)
        return s

    def __repr__(self):
        """ Return a string representation of the rectangle"""
        a = "Rectangle({}, {})".format(self.__width, self.__height)
        return eval(repr("{}".format(a)))

    def __del__(self):
        print("Bye rectangle...")
