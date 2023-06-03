#!/usr/bin/python3
"""
class Base:

private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute
    id with this argument value - you can assume id is an
    integer and you dont need to test the type of it
otherwise, increment __nb_objects and assign the new
    value to the public instance attribute id
"""
import json


class Base():
    """Base class for all shapes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Func to make into json file"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Func to write json str to file"""
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))
            