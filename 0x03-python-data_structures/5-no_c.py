#!/usr/bin/env python3
def no_c(my_string):
    characters = "Cc"

    my_string = ''.join(x for x in my_string if x not in characters)

    return my_string
