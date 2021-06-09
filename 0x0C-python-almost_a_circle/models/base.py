#!/usr/bin/python3
"""class Base"""
import json


class Base:
    """is a comment"""

    __nb_objects = 0

    def __init__(self, id=None):
        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Add fuc JSON 1 """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """add func JSON 2"""

        c = []
        name = cls.__name__ + ".json"

        if list_objs is not None:
            for i in list_objs:
                c.append(cls.to_dictionary(i))

        with open(name, mode="w") as file:
            file.write(cls.to_json_string(c))
