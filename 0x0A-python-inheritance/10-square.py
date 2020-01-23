#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
