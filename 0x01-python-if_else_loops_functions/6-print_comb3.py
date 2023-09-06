#!/usr/bin/python3
for num in range(0, 100):
    if num > 9:
        if str(num)[0] == str(num)[1] or str(num)[0] > str(num)[1]:
            continue
    elif int(num) == 0:
        continue
    else:
        num = f"{num:02d}"
    if int(num) < 89:
        print("{}, ".format(num), end='')
    else:
        print("{}".format(num))
