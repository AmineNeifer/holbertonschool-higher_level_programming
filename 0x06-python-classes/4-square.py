#!/usr/bin/python3


class Square:

    def __init__(self, size=0):
        """Args:
               size: size of the Square.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns:
                the area of the square (size)
        """
        return self.__size * self.__size
