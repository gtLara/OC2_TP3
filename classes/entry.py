"""Define classe Entry.

Entidade representa uma entrada ou "linha" da cache,
com os dados e informações necessárias para sua operação.

"""
from utils import create_storage
from math import log

class Entry:

    def __init__(self, n_index_bits=6, block_size=4):

        self.n_index_bits = n_index_bits
        self.block_size = block_size

        self.dirty_bit = 0
        self.valid_bit = 0
        self.index = 0
        self.tag = 0

        self.block = create_storage(block_size, 0)
