#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    j = 0
    a = 0
    for i in argv[1:]:
        j += int(i)
    print(j)
