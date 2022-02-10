"""Define classe Cache."""
from math import log, ceil
import copy
from classes.entry import Entry
from classes.utils import create_storage

class Cache:

    def __init__(self, n_blocks=64, block_size=4):

        assert not (log(n_blocks, 2) % 1) # assert n_blocks is power of 2

        self.block_size = block_size
        self.n_set_bits = int(log(n_blocks, 2))
        self.n_block_offset_bits = ceil(log(block_size, 2))

        self.entries = create_storage(n_blocks,
                                      Entry,
                                      self.n_set_bits,
                                      block_size)

    def decompose_address(self, cpu_address):
        """Decompõe endereços de CPU em campos relevantes."""

        bo_upper = -(self.n_block_offset_bits)
        block_offset = cpu_address[bo_upper:]

        index_lower = bo_upper
        index_upper = bo_upper - self.n_set_bits

        index = cpu_address[index_upper:index_lower]

        tag_lower = index_upper

        tag = cpu_address[:tag_lower]

        return block_offset, index, tag

    def read(self, cpu_address, memory, verb=True):

        block_offset, index, tag = self.decompose_address(cpu_address)
        entry = self.entries[index]

        if entry.valid_bit and entry.tag == tag: # hit, OK
            status = "H"
            if verb:
                print("cache read HIT")

            word = entry.block[block_offset]

        else:
            status = "M"
            if verb:
                print("cache read MISS")

            if entry.dirty_bit == 1:
                memory.write_block(index, entry.tag, entry)

            self.entries[index].valid_bit = 1
            self.entries[index].dirty_bit = 0
            self.entries[index].tag = tag

            memory_address = int(cpu_address[-(memory.address_size):], 2)

            memory_address = memory_address - (memory_address % self.block_size)
            memory_address = format(memory_address, f"0{memory.address_size}b")

            block = memory.read_block(memory_address, block_size=self.block_size)
            self.entries[index].block = block
            word = block[block_offset]

        return word, status

    def write_entry(self, data, index, block_offset, dirty, tag):

        wentry = self.entries[index]
        wentry.block[block_offset] = data
        wentry.valid_bit = 1
        wentry.dirty_bit = dirty
        wentry.tag = tag

    def write(self, cpu_address, data, memory, verb=True):

        block_offset, index, tag = self.decompose_address(cpu_address)
        entry = self.entries[index]
        memory_address = cpu_address[-(memory.address_size):]

        if entry.valid_bit and entry.tag == tag: # hit
            if verb:
                print("cache WRITE HIT")

            if entry.dirty_bit == 0: # case in which cache block corresponds to memory block

                dirty = 1 # indicates that cache block does not represent memory
                self.write_entry(data, index, block_offset, dirty, tag)

            else: # case in which cache block does not mirror memory

                dirty = 0 # indicates that cache block corresponds to memory
                self.write_entry(data, index, block_offset, dirty, tag)
                memory.write_block(index, tag, entry)

        else:
            if verb: # think this one through
                print("cache WRITE MISS")

                memory_address = int(memory_address, 2)

                memory_address = memory_address - (memory_address % self.block_size)
                memory_address = format(memory_address, f"0{memory.address_size}b")

                block = memory.read_block(memory_address, block_size=self.block_size)
                self.entries[index].block = block

                dirty = 1
                self.write_entry(data, index, block_offset, dirty, tag)
                # memory.write_block(index, tag, entry)

    def __str__(self):

        cache_vis = " INDEX  | V | D | TAG      |  DATA\n"

        for entry in self.entries.values():
            cache_vis += (str(entry)+"\n")

        return cache_vis

    def __getitem__(self, slice_key):

        sliced_cache = copy.deepcopy(self)
        new_entries = dict(list(self.entries.items())[slice_key])
        sliced_cache.entries = new_entries
        return sliced_cache
