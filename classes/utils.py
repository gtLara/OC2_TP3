from math import log
import random

def int_2_padded_bin(integer, pad_up_to):
    """Converte número inteiro em string binária.

    A string resultante é preenchida de zeros à esquerda até
    que contenha o número de bits especificado por pad_up_to.

    Ex: int_2_padded_bin(8, 6) -> "001000"

    """

    binary_string = "{0:#b}".format(integer).replace("0b", "")
    padding = "0" * (pad_up_to - len(binary_string))
    binary_string = padding + binary_string

    return binary_string

def create_random_word(size=32):

    word = ""
    for i in range(size):
        word += str(random.randint(0, 1))

    return word

def create_storage(n_items, initial_data="0"):

    data = {}
    n_index_bits = int(log(n_items, 2))

    for item_index in range(n_items):

        binary_string_index = int_2_padded_bin(item_index, n_index_bits)

        if callable(initial_data): # case in which initial_data is function
            data[binary_string_index] = initial_data()
        else:
            data[binary_string_index] = initial_data

    return data
