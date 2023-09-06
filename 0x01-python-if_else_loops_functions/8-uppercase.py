#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char >= 'a' and char <= 'z':
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            upper_char = char
        print("{}".format(upper_char), end='')
    print()
