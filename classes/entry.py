"""Define classe Entry.

Entidade representa uma entrada ou "linha" da cache,
com os dados e informações necessárias para sua operação.

"""
from math import log

class Entry:

    def __init__(self, n_index_bits, n_tag_bits, block_size):

        self.n_index_bits = n_index_bits
        self.n_tag_bits = n_tag_bits
        self.block_size = block_size

        self.dirty_bit = 0
        self.valid_bit = 0
        self.index = 0
        self.tag = 0
        self.block = {}
        n_bits_block_index = int(log(block_size, 2))

        for word_index in range(block_size):
            binary_string_index = "{0:#b}".format(word_index).replace("0b", "")
            padding = "0" * (n_bits_block_index - len(binary_string_index))
            binary_string_index = padding + binary_string_index
            self.block[binary_string_index] = 0
