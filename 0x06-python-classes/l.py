#!/usr/bin/python3
"""Defines a class as Square"""


class Square:
    """ Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes the square"""
        self.size = size

    @property
    def size(self):
        """getter of __size"""
        return self.__size

    @property
    def position(self):
        """getter of __size"""
        return self.__position

    @size.setter
    def size(self, value):
        """setter of __size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @size.setter
    def position(self, value):
        """setter of __size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.position = value

    def my_print(self):
        """that prints in stdout the square with"""
        if self.size != 0:
            if self.position[1] is not 0:
                print('\n' * self.position[1], end= "")
            for z in range(self.size):
                print(" " * self.position[0], end=" ")
                print(" " * self.size, end=" ")
        else:
            print()
    def area(self):
        """ Returns the current square area """
        return (self.__size) ** 2
