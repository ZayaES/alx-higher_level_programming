#!/usr/bin/python3
# Author: Zaya Bell

"""Defines a function which creates 
    python object from json strings .

    """


import json


def from_json_string(my_str):
    """converts json format to python object """

    f = json.loads(my_str)
    return f
