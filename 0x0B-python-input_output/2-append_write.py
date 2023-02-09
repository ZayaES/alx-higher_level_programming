#!/usr/bin/python3
# Author: Zaya Bell

"""Creates a function that appends to a  file"""


def append_write(filename="", text=""):
    """A wrapper function for .write() method."""

    with open(filename, "a", encoding="utf-8") as opened_file:
        return (opened_file.write(text))
