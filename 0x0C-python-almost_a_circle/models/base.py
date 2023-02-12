#!/usr/bin/python3
# Author: Zaya Bell

class Base:
    """Acting as a Base class for other classes
        in this project. Manages id attribute for
        all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """instance of Base are initialized as follows:
            if id is None(null) increment __nb_objects
            and assignt to id
            else, assign the input id as id.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
