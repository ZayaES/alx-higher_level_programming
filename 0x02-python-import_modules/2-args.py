#!/usr/bin/python3
from sys import argv
x = len(argv) - 1
if x == 0:
    print("{} arguments.".format(x))
elif x == 1:
    print("{} argument:".format(x))
elif x > 1:
    print("{} arguments:".format(x))
y = 1
for i in argv[1:]:
    print("{}: {}".format(y, i))
    y += 1
