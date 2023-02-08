#!/usr/bin/python3
# Author: Zaya Bell

""" Defines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ creates a shape square which inherits rectangle"""

    def __init__(self, size):
        """initializes square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
