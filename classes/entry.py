"""Define classe Entry.

Entidade representa uma entrada ou "linha" da cache,
com os dados e informações necessárias para sua operação.

"""
from classes.utils import create_storage, create_random_word
from math import log

class Entry:

    def __init__(self, n_index_bits=6, block_size=4, index=0, random=True):

        self.n_index_bits = n_index_bits
        self.block_size = block_size
        self.index = index

        self.dirty_bit = 0
        self.valid_bit = 0
        self.block = {}
        self.tag = 0

        if random:
            self.block = create_storage(block_size, create_random_word)
        else:
            self.block = create_storage(block_size)

    def __str__(self):

        hex_block = {}

        for key, value in self.block.items():
            hex_block[key] = hex(int(value, 2))

        return f" {self.index} | {self.valid_bit} | {self.dirty_bit} | {self.tag} | {hex_block}"
