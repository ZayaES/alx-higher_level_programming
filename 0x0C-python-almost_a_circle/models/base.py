#!/usr/bin/python3
# Author: Zaya Bell
""" This is a module which defines a base class.
    Main purpose is to act as a superclass and gives
    id to instances

    """


import json

class Base:
    """Acting as a Base class for other classes
        in this project. Manages id attribute for
        all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """instance of Base are initialized as follows:
            if id is None(null) increment __nb_objects
            and assignt to id
            else, assign the input id as id.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1,1)
            else:
                new_intance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except IOError:
            return []
