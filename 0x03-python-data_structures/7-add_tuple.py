#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = []
    for i in range(2):
        if i >= len(tuple_b) and i >= len(tuple_a):
            tuple_c.append(0)
        elif i >= len(tuple_a):
            tuple_c.append(0 + tuple_b[i])
        elif i >= len(tuple_b):
            tuple_c.append(0 + tuple_a[i])
        else:
            tuple_c.append(tuple_a[i] + tuple_b[i])

    return tuple(tuple_c)
