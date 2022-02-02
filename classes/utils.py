from math import log

def create_storage(n_items, initial_data="0"):

    data = {}
    n_index_bits = int(log(n_items, 2))

    for item_index in range(n_items):
        binary_string_index = "{0:#b}".format(item_index).replace("0b", "")
        padding = "0" * (n_index_bits - len(binary_string_index))
        binary_string_index = padding + binary_string_index
        data[binary_string_index] = initial_data

    return data
