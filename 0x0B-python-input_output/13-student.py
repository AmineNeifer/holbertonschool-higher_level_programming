#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            dic = {}
            for i, j in self.__dict__.items():
                if i in attrs:
                    dic[i] = j
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        self.__dict__ = json
