#!/usr/bin/python3
"""Defines a class as Square"""


class Square:
    """ Represents a square"""

    def __init__(self, size=0):
        """initializes the square"""
        self.size = size

    @property
    def size(self):
        """getter of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """that prints in stdout the square with"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                    print("".join(["#"for x in range(self.__size)]))

    def area(self):
        """ Returns the current square area """
        return (self.__size) ** 2
