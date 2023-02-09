#!/usr/bin/python3
# Author: Zaya Bell

"""Creates a function that appends to a  file"""


def append_file(filename="", text=""):
    """A wrapper function for .write() method."""

    with open(filename, "a", encoding="utf-8") as new_file:
        return (new_file.write(text))
