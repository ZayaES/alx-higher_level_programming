#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    cp_list = my_list.copy()
    cp_list.insert(idx, element)
    del cp_list[idx + 1]
    return cp_list
