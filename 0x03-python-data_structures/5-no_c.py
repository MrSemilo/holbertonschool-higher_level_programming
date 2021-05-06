#!/usr/bin/env python3
def no_c(my_string):
    characters = "Cc"

    new_string = ''.join(x for x in my_string if x not in characters)

    return new_string
