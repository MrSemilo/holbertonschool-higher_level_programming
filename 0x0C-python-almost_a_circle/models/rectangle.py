#!/usr/bin/python3
"""class Rectangle add x and y"""

from models.base import Base


class Rectangle(Base):
    """def init"""

    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Rectangle of __width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Returns"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute."""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Returns"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute."""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the rectangle area"""
        return (self.height * self.width)

    def display(self):
        """ Print the rectangle with the character #"""
        x = ""
        a = "{}".format(self.print_symbol)
        if self.__height == 0 or self.__width == 0:
            print(x)
        for i in range(0, self.__height):
            if i < self.__height - 1:
                x = x + (a * self.__width + "\n")
            else:
                x = x + (a * self.__width)
        print(x)

    def __str__(self):
        i = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return i
