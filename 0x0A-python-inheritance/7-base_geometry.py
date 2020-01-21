#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        """ Raises: Exception: if area is not implemented. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Raise:
                TypeError: if value is not int
                ValueError: if int is less or equal to zero
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
