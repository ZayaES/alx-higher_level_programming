#!/usr/bin/python3
# Author: Zaya Bell

"""Defines a class MyList which inherits from class List"""


class MyList(list):
    """Defines MyList as a List such that it inherits the
    attribute and methods of List

    """

    def print_sorted(self):
        """sorts out list in ascending order"""

        print(sorted(self))      
