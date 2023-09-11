#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        c = 0
        for cell in ligne:
            if c < len(ligne) - 1:
                print("{:d}".format(cell), end=' ')
                c += 1
            else:
                print("{:d}".format(cell), end='$')
        print()
