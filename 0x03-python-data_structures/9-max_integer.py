#/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_v = my_list[0]
        for i in range(1, len(my_list)):
            if max_v < my_list[i]:
                max_v = my_list[i]
        return (max_v)
    return None
