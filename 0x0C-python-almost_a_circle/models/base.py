#!/usr/bin/python3
""" Base class is the most super class in this project """


import json


class Base:
    """ conatins methods to all kinds of geometry shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ takes an objects and converts it to a json string"""
        if list_dictionaries is not None and len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ takes a json string and writes it in a json file properly"""
        l = []
        name = cls.__name__
        with open('{}.json'.format(name), 'w', encoding="utf-8") as f:
            if list_objs is not None:
                for i in list_objs:
                    i = i.to_dictionary()
                    l.append(i)
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """ converts contents of a json file to string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates list of dictionaries of a json tring"""
        if cls.__name__ = "Rectangle":
            dummy = cls(1, 1, 1)
        else:
            dummy = cls(1, 1)
        i = [1, 2, 3, None, None]
        for k, v in dictionary.items():
            if k == "id":
                i[0] = v
            elif k == "width":
                i[1] = v
            elif k == "height":
                i[2] = v
            elif k == "x":
                i[3] = v
            elif k == "y":
                i[4] = v
        t = tuple(i)
        dummy.update(*t)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ takes a file and creates instances out of it"""
        with open('{}.json'.format(cls.__name__), 'r', encoding="utf-8") as f:
            loaded_str = cls.from_json_string(f.read())
        l = []
        for i in loaded_str:
            created = cls.create(**i)
            l.append(created)
        return l
