#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        c = 0
        for cell in ligne:
            print("{:d}".format(cell), end=' ')
            c += 1
        print()
