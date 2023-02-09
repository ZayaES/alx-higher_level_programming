#!/usr/bin/python3
# Author: Zaya Bell

"""Defines a function which creates json string
    from python object.

    """


import json


def to_json_string(my_obj):
    """converts python object to json format"""

    f = json.dumps(my_obj)
    return f
