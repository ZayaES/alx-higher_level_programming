#!/usr/bin/python3
# Author: Zaya Bell

"""Defines a function which creates json string
    from python object.

    """


import json


def save_to_json_file(my_obj, filename):
    """converts python object to json format
    and saves in a file

    """
    with open(filename, "w", encoding="utf-8") as new:
        f = json.dump(my_obj, new)
        return f
