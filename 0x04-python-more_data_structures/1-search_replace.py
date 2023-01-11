#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ changes entries of a list"""
    f = lambda x: replace if (x == search) else x
    return list(map(f, my_list))
