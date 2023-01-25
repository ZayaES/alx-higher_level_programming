#!/usr/bin/python3
"""This is a module that creates a class
based on 3-square.py

"""


class Square(object):
    """A class that takes an input

    """
    def __init__(self, size=0, position=(0, 0)):
        """the init module which initializes
        the instance of the class

        """
        self.__size = size
        self.__position = position
        try:
            range(0, self.__size)
        except Exception:
            raise TypeError("size must be an integer")
        else:
            if int(self.__size < 0):
                raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square given the size

        """
        return self.__size ** 2

    @property
    def size(self):
        """a method which retrieves the instance private
        instance attribute size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of the instance private
        attribute size

        """
        try:
            range(0, value)
        except Exception:
            raise TypeError("size must be an integer")
        else:
            if int(value < 0):
                raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the current posion of the square specified
        by size

        """
        return (self.__position)

    @position.setter
    def postion(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square using the # character

        """
        if self.__size == 0:
            print()
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("_", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
