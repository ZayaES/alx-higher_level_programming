#!/usr/bin/python3

def find_peak(list_of_integers):
    """finds a peak in an unordered list of integers"""
    n_max = max(list_of_integers)
    max_index = list_of_integers.index(n_max)
    return n_max
    """try:
        left = list_of_integers[max_index - 1]
    except IndexError:
        list_of_integers.remove(n_max)
        n_max = max(list_of_integers)
    try:
        right = list_of_integers[max_index + 1]
    except IndexError:
        if (list_of_integers[max_index - 1]
            and list_of_integers[max_index + 1]):
"""
