#!/usr/bin/python3
# Author: Zaya Bell

"""Defines a function which creates
    python object from json file.

    """


import json


def load_from_json_file(filename):
    """converts json format to python object """
    with open(filename, "r", encoding="utf-8") as new:
        f = json.load(new)
        return f
