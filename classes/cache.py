"""Define classe Cache."""
from math import log, ceil

class Cache:

    def __init__(self, n_blocks=64, block_size=4):

        assert not (log(n_blocks, 2) % 1) # assert n_blocks is power of 2

        self.n_set_bits = int(log(n_blocks, 2))
        self.n_block_offset_bits = ceil(log(block_size, 2))
        # self.n_bits_secondary_address = self.n_set_bits + self.n_block_offset_bits #TODO: understand whats up here

    def decompose_address(self, raw_address):
        """Decompõe endereços de CPU em campos relevantes."""

        byte_offset = raw_address[-2:]

        bo_lower = -2
        bo_upper = -(self.n_block_offset_bits+2)
        block_offset = raw_address[bo_upper:bo_lower]

        index_lower = bo_upper
        index_upper = bo_upper - self.n_set_bits

        index = raw_address[index_upper:index_lower]

        tag_lower = index_upper

        tag = raw_address[:tag_lower] #TODO: understand whats up here

        return byte_offset, block_offset, index, tag
