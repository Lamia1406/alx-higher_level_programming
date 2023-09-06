#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    while number > 9:
        number %= 10
    print(f"{number:d}", end='')
    return number
