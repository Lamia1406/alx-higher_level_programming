#!/usr/bin/python3
for c in range(ord('A'), ord('Z') + 1):
    print("{:c}".format(c), end='' if c < ord('Z') else '\n')
