#!/usr/bin/python3
i = 0
for alp in reversed(range(97, 123)):
        if i % 2 == 0:
            print("{}".format(chr(alp)), end="")
        else:
            print("{}".format(chr(alp - 32)), end="")
        i += 1
