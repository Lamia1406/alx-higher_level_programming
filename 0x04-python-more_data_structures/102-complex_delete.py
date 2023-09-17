#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for k in a_dictionary.keys():
        if a_dictionary[k] == value:
            keys.append(k)
    for k in keys:
        del a_dictionary[k]
    return a_dictionary
