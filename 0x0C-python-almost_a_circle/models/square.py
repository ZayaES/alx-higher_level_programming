#!/usr/bin/python3
# Author: Zaya Bell

"""Defines a class Square which inherits
    attributes of rectangle

    """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Create an instance of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""

        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        for key in kwargs:
            if key == "id" and len(args) < 1:
                self.id = kwargs[key]
            if key == "size" and len(args) < 2:
                self.width = self.height = kwargs[key]
            if key == "x" and len(args) < 3:
                self.x = kwargs[key]
            if key == "y" and len(args) < 4:
                self.y = kwargs[key]

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""

        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Return the print() and str() representation of a Square."""

        string = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                   self.width)
        return string
