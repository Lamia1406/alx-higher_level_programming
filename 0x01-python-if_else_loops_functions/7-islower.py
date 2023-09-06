#!/usr/bin/python3
def islower(c):
    for char in range(ord('a'), ord('z') + 1):
        if chr(char) == c:
            return True
    return False
