#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for key in a_dictionary.keys():
        biggest_key = key
        break
    for key in a_dictionary.keys():
        if key > biggest_key:
            biggest_key = key
    return biggest_key
