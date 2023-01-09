#!/usr/bin/python3
def no_c(my_string):
    u = 0
    new = my_string
    for i in new:
        if (i == chr(67) or i == chr(99)):
            new = new[:u] + new[u + 1:]
        else:
            u += 1
    return new
