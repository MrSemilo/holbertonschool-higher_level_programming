def replace_in_list(my_list, idx, element):
    list = len(my_list)

    if idx >= 0 and idx < list:
        my_list[idx] = element
    return my_list
