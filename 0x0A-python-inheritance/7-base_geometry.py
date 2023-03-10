#!/usr/bin/python3
# Author: Zaya Bell

"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Raises an error when area is called"""

    def area(self):
        """Raises error"""
        
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))

        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
