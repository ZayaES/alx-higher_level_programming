#!/usr/bin/python3
# Author: Zaya Bell
"""Defines a rectangle which inherits from Base
    given in base.py
    """

from models.base import Base

class Rectangle(Base):
    """describes a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes objects as  rectangle

        arguments:
        width: rectangle's width
        height: rectangle's height
        x: x-cordinate (position of the top left corner of the rectangle) 
        y: y-cordinate
        id: identification of the instance

        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Returns the area of the instance object"""

        return self.__width * self.__height
    
    def display(self):
        """Prints the rectangle with character # to 
            stdout

            """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        string = "[Rectangle] (" + str(self.id) + ") " + str(self.__x)
        string += "/" + str(self.__y) + " - " + str(self.__width) + "/"
        string += str(self.__height)
        return string
    
    def update(self, *args, **kwargs):
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

        for key in kwargs:
            if key == "id" and len(args) < 1:
                self.id = kwargs[key]
            if key == "width" and len(args) < 2:
                self.__width = kwargs[key]
            if key == "height" and len(args) < 3:
                self.__height = kwargs[key]
            if key == "x" and len(args) < 4:
                self.__x = kwargs[key]
            if key == "y" and len(args) < 5:
                self.__y = kwargs[key]

    def to_dictionary(self):
        return {
                "id": self.id,
                "y": self.y,
                "x": self.x,
                "height": self.height,
                "width": self.width
                }
