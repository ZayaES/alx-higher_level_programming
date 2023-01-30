#!/usr/bin/python3
# Written by Zaya Bell"

"""Defines a Rectangle class
This class can specify the height and width of a rectangle

"""


class Rectangle:
    """Defines a rectangle with optional width and height


    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value is None:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value is None:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of an instance rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of an instance rectangle """
        if self.__width == 0 || self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
