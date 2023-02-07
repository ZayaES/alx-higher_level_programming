#!/usr/bin/python3
# Author: Zaya Bell

"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Raises an error when area is called"""

    def area(self):
        raise Exception("area() is not implemented")
