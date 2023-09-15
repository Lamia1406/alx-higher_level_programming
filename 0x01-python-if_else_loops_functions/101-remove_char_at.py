#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for c in str:
        if n < len(str) and n >= 0 and c == str[n]:
            continue
        else:
            new_str += c
    return new_str
