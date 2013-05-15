def custom_remove(input_list, value):
    """custom_remove(input_list, value) imitates input_list.remove(value)"""
    i = 0
    for item in input_list:
        if item == value:
            del input_list[i]
        i += 1
