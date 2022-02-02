"""Define classe Cache."""
from math import log, ceil
from entry import Entry
from utils import create_storage

class Cache:

    def __init__(self, n_blocks=64, block_size=4):

        assert not (log(n_blocks, 2) % 1) # assert n_blocks is power of 2

        self.n_set_bits = int(log(n_blocks, 2))
        self.n_block_offset_bits = ceil(log(block_size, 2))
        # self.n_bits_secondary_address = self.n_set_bits + self.n_block_offset_bits #TODO: understand whats up here

        self.entries = create_storage(n_blocks,
                                      Entry(self.n_set_bits, block_size))

    def decompose_address(self, cpu_address):
        """Decompõe endereços de CPU em campos relevantes."""

        byte_offset = cpu_address[-2:]

        bo_lower = -2
        bo_upper = -(self.n_block_offset_bits+2)
        block_offset = cpu_address[bo_upper:bo_lower]

        index_lower = bo_upper
        index_upper = bo_upper - self.n_set_bits

        index = cpu_address[index_upper:index_lower]

        tag_lower = index_upper

        tag = cpu_address[:tag_lower] #TODO: understand whats up here

        return byte_offset, block_offset, index, tag

    def read(self, cpu_address): # TODO: check

        byte_offset, block_offset, index, tag = self.decompose_address(cpu_address)
        entry = self.entries[index]

        if entry.valid_bit and entry.tag == tag: # hit
            word = entry.block[block_offset]

            return word

        else:
            pass
            # memory_system.get_data(cpu_address)

    def write(self, cpu_address, data):
        pass
