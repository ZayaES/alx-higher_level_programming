#!/usr/bin/python3
# Author: Zaya Bell

"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a shape Rectangle which inherits BaseGeometry"""

    def __init__(self, width, height):
        """initializes rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.interger_validator("height", height)
        self.__height = height
