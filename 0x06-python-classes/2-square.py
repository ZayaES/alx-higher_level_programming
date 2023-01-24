#!/usr/bin/python3
"""This is a module that creates a class
based on 0-square.py

"""


class Square(object):
    """A class that takes an input

    """
    def __init__(self, size=0):
        """the init module which initializes
        the instance of the class

        """
        self.__size = size
        try:
            range(0, self.__size)
        except Exception:
            raise TypeError("size must be an integer")
        else:
            if int(self.__size < 0):
                raise ValueError("size must be >= 0")
