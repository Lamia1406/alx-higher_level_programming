#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    try:
        for i in range(x):
            result = result * 10 + my_list[i]
        print(result)
        return x
    except(IndexError):
        print(result)
        return i
