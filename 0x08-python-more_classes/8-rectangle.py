#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """empty"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle"""
        self.height = height
        self.width = width

        Rectangle.number_of_instances += 1

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
        x = ""
        a = "{}".format(self.print_symbol)
        if self.__height == 0 or self.__width == 0:
            return x
        for i in range(0, self.__height):
            if i < self.__height - 1:
                x = x + (a * self.__width + "\n")
            else:
                x = x + (a * self.__width)
        return x

    def __repr__(self):
        """ Return a string representation of the rectangle"""
        a = "Rectangle({}, {})".format(self.__width, self.__height)
        return eval(repr("{}".format(a)))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not type(rect_1) is Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not type(rect_2) is Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        a = rect_1.area()
        b = rect_2.area()
        if a >= b:
            return rect_1
        else:
            return rect_2
