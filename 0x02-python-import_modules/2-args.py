#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    print("{} argument".format(args), end='')
    if args == 0 or args > 1:
        print("s:")
    elif args == 1:
        print(":")
    if args >= 1:
        for i in range(1, args + 1):
            print("{}: {}".format(i, sys.argv[i]))
