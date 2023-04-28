#!/usr/bin/python3
"""Module contains a function that finds the peak
in an unordered list of integer"""


def find_peak(list_of_integers):
    """finds a peak in an unordered list of integers"""

    ans = None
    while(ans is None and list_of_integers is not None):
        if len(list_of_integers) == 1 or len(list_of_integers) == 2:
            return max(list_of_integers)
        if len(list_of_integers) == 0:
            return None
        ans = check_start(list_of_integers)
        if ans is not None:
            return ans
        ans = check_end(list_of_integers)
        if ans is not None:
            return ans
        ans = check_left(list_of_integers)
        if ans is not None:
            return ans
        ans = check_right(list_of_integers)
        if ans is not None:
            return ans
        del (list_of_integers[0])
        del (list_of_integers[1])
    return None

def check_start(list_):
    """ checks for peak in the first 2 numbers"""

    if (list_[0] < list_[1] and list_[2] < list_[1]):
        return list_[1]
    elif list_[0] > list_[1]:
        return list_[0]
    else:
        return None


def check_end(list_):
    """ checks for peak in the last 2 numbers"""

    if (list_[-3] < list_[-2] and list_[-1] < list_[-2]):
        return list_[-2]
    elif list_[-1] > list_[-2]:
        return list_[-1]
    else:
        return None


def check_left(list_):
    """checks for peak on the left side of centre"""

    half = len(list_) // 2
    while (half > 1):
        if list_[half] > list_[half - 1] and list_[half] > list_[half + 1]:
            return list_[half]
        half = half // 2
    return None


def check_right(list_):
    """checks for peak on the right side of centre"""

    half = len(list_) // 2
    while (half < len(list_) - 2):
        if list_[half] > list_[half - 1] and list_[half] > list_[half + 1]:
            return list_[half]
        half = half + (len(list_) - half) // 2
    return None
