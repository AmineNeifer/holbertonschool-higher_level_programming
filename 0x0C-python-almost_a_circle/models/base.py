#!/usr/bin/python3
""" Base class is the most super class in this project """


import json
import turtle
import random

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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ takes a file and creates instances out of it"""
        l = []
        name = cls.__name__
        try:
            with open('{}.json'.format(name), 'r', encoding="utf-8") as f:
                loaded_str = cls.from_json_string(f.read())
        except:
            return l

        for i in loaded_str:
            created = cls.create(**i)
            l.append(created)
        return l

    @staticmethod
    def draw(list_rectangles, list_squares):
        for i in list_rectangles:
            rand1 = random.randrange(-350,350)
            rand2 = random.randrange(-350,350)
            nok = turtle.Turtle()
            nok.speed(1)
            nok.color('yellow', 'red')
            nok.pensize(10)
            nok.shape('turtle')
            nok.penup()
            nok.setpos(rand1, rand2)
            nok.pendown()
            nok.forward(i.width)
            nok.left(90)
            nok.forward(i.height)
            nok.left(90)
            nok.forward(i.width)
            nok.left(90)
            nok.forward(i.height)
        for i in list_squares:
            squa = turtle.Turtle()
            squa.speed(1)
            squa.pensize(8)
            squa.shape('turtle')
            squa.color('green', 'orange')
            rand1 = random.randrange(-350,350)
            rand2 = random.randrange(-350,350)
            squa.penup()
            squa.setpos(rand1, rand2)
            squa.pendown()
            squa.begin_fill()
            for x in range(4):
                squa.forward(i.size)
                squa.left(90)
            squa.end_fill()
