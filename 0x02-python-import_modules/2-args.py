#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    c = len(argv) - 1
    a = len(argv)
    if c == 0:
        print("{} arguments.".format(c))

    else:
        if c == 1:
            print("{} argument:".format(c))
        else:
            print("{} arguments:".format(c))

        for i in range(1, a):
            print("{:d}: {:s}".format(i, argv[i]))
