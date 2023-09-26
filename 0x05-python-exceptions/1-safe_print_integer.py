#!/usr/bin/python3
def safe_print_integer(value):
    result = 0
    try:
        print("{:d}".format(value))
        return True
    except(ValueError):
        return False