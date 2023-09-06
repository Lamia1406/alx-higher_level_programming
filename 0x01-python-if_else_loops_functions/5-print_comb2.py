#!/usr/bin/python3
for num in range(0, 100):
    if num < 10:
        num = f"{num:02d}"
    if num == 99:
        print("{}".format(num))
    else:
        print("{}, ".format(num), end='')
