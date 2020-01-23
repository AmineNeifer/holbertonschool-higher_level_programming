#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
