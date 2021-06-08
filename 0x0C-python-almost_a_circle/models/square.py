#!/usr/bin/python3
"""class square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """__int__"""
        self.size = size
        super().__init__(size, size,  x,  y,  id)

    def __str__(self):
        """__str__"""
        str_ = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__width)

        return str_

    @property
    def size(self):
        """property"""
        return self.__width

    @size.setter
    def size(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """update"""

        if not args or len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

        else:
            for i in range(len(args)):

                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.size = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
                else:
                    break

    def to_dictionary(self):
        """to_dictionary"""
        my_dict = {'id': self.id, 'size': self.size,
                   'x': self.x, 'y': self.y}
        return my_dict
