#!/usr/bin/python3
for num in range(0, 100):
    if num > 9:
        if str(num)[0] == str(num)[1] or str(num)[0] > str(num)[1]:
            continue
    elif num == 0:
        continue
    else:
        num = f"{num:02d}"
    print("{}, ".format(num), end='')
print("")
