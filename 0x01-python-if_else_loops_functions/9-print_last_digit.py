#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0 or (number % 10 == 0):
        last_dig = number % 10
    else:
        last_dig = 10 - (number % 10)

    print("{}".format(last_dig), end="")
    return last_dig
        
