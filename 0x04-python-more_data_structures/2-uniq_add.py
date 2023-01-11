#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_ = 0
    f = set(my_list)
    for i in f:
        sum_ = sum_ + i
    return sum_
