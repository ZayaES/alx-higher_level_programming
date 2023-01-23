#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as exp_mes:
        print("Exception: {}".format(exp_mes), file=sys.stderr)
        return None
