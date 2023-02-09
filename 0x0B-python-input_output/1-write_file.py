#!/usr/bin/python3
# Author: Zaya Bell

"""Creates a function that writes to a  file"""


def write_file(filename="", text=""):
    """A wrapper function for .read() method."""

    with open(filename, "w", encoding="utf-8") as new_file:
        return (new_file.write(text))

