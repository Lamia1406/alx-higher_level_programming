#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        c = 0
        for cell in ligne:
            if c < len(ligne) - 1:
                print("{:d}".format(cell), end=' ')
            else:
                print("{:d}".format(cell))
            c += 1
