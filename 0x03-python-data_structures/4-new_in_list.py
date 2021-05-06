#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list = len(my_list)
    list_new = my_list.copy()

    if idx >= 0 and idx < list:
        list_new[idx] = element
    return list_new
