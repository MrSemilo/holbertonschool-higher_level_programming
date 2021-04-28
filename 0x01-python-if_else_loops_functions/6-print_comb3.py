#!/usr/bin/python3

for c in range(0, 10):
    for i in range(1, 10):
        if c == 8 and i == 9:
            print("{}{}".format(c, i))
        elif c < i:
            print("{}{}, ".format(c, i), end="")
