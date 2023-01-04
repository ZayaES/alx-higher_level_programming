#!/usr/bin/python3
for i in range(0, 8):
    for j in range(1, 10):
        if (i < j):
            print("{:0=2d}".format((10 * i) + j), end=", ")

print("{:0=2d}".format(89))
