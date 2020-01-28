#!/usr/bin/python3
""" Rectangle: sublcass of Base.
    
    dimensions: width, height, x and y"""


from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)       
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """ Returns: the area of our rectangle which is
        the width and height multiplied together. """
        return self.__width * self.__height

    def display(self):
        """ prints our rectangle in hashes '#' """
        for i in range(self.__y):
            print()
        for i in range (self.__height):
            print (self.__x * " " + self.__width * "#")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - \
{}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self, *args, **kwargs):
        count = 0
        list = [self.id, self.__width, self.__height, self.__x, self.__y]
        if len(args) != 0:
            for i in args:
                if count == 0:
                    self.id = i
                elif count == 1:
                    self.__width = i
                elif count == 2:
                    self.__height = i
                elif count == 3:
                    self.__x = i
                elif count == 4:
                    self.__y = i
                count += 1
        else:
            for k, v in kwargs.items():
                if k == 'width':
                    self.__width = v
                elif k == 'height':
                    self.__height = v
                elif k == 'x':
                    self.__x = v
                elif k == 'y':
                    self.__y = v
                elif k == 'id':
                    self.id = v

    def to_dictionary(self):
        dicc = {}
        dicc['x'] = self.__x
        dicc['y'] = self.__y
        dicc['id'] = self.id
        dicc['width'] = self.__width
        dicc['height'] = self.__height
        return dicc
