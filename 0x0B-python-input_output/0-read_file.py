#!/usr/bin/python3
# Author: Zaya Bell

"""Creates a function that reads file"""


def read_file(filename=""):
    """A wrapper function for .read() method."""

    with open(filename, "r", encoding="utf-8") as new_file:
        print(new_file.read(), end="")
