#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ changes entries of a list"""
    return list(map(lambda x: replace if (x == search) else x, my_list))
