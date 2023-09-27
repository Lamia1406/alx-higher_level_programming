#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        num = 0
        while i < x:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end='')
                num += 1
            i += 1
        print()
        return num
    except (ValueError, TypeError):
        print()
        return num
