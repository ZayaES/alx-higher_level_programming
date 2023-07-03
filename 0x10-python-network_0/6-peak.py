#!/usr/bin/python3
""" finds the peak in a list of number with low time complexity"""


def find_peak(list_of_integers):
    """ finds the peak in list_of_integers"""
    if (not list_of_integers):
        return None
    if (len(list_of_integers) < 4):
        return max(list_of_integers)
    while((len(list_of_integers)) != 0):
        result = check_start(list_of_integers)
        if (result):	
            return result
        result = check_end(list_of_integers)
        if (result):
    	    return result
        result = check_left(list_of_integers)
        if (result):
            return result
        result = check_right(list_of_integers)
        if (result):
            return result
        del list_of_integers[-1]

def check_start(list_):
    """ checks if peak is at start of list """
    if (list_[0] > list_[1]):
        return list_[0]
    elif (list_[1] > list_[0] and list_[1] > list_[2]):
        return list_[1]

def check_end(list_):
    """ checks if peak is at end of list"""

    if (list_[-1] > list_[-2]):
        return list_[-1]
    elif (list_[-2] > list_[-1] and list_[-2] > list_[-3]):
        return list_[-2]

def check_left(list_):
    """ checks LHS from centre until end in binary format"""

    sz = len(list_)
    while (sz > 1):
        if (sz % 2) == 0:
            sz = sz // 2
        else:
            sz = (sz - 1) // 2

        if (list_[sz] > list_[sz + 1]) and \
            (list_[sz] > list_[sz - 1]):
            return list_[sz]

def check_right(list_):
    """ checks RHS from centre until end in binary format"""
    sz = len(list_)
    while (sz < len(list_) - 1):
        if (sz % 2) == 0:
            sz = sz // 2
        else:
            sz = (sz + 1) // 2
        
        RH = len(list_) - sz
        if (RH % 2 == 0):
            add = RH // 2
        else:
            add = (RH - 1) // 2

        if (list_[sz + add] > list_[sz + add - 1]) and \
            (list_[sz + add] > list_[sz + add - 1]):
            return list_[sz + add]
