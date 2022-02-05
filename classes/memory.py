from math import log
import copy
from classes.utils import create_storage, create_random_word, int_2_padded_bin

class PhysicalMemory:

    def __init__(self, n_words=1024, word_size=32, random=True):

        self.n_words = n_words
        self.address_size = int(log(n_words, 2))

        if random:
            self.data = create_storage(n_words,
                                       init_data=create_random_word)
        else:
            self.data = create_storage(n_words)

    def read_block(self, address, block_size=4): # TODO: review spread policy

        assert len(address) == self.address_size

        block = create_storage(block_size)

        for k, key in enumerate(block.keys()):

            word_address = int(address, 2) + k

            assert word_address < self.n_words

            word_address = int_2_padded_bin(word_address, self.address_size)

            block[key] = self.data[word_address]

        return block

    def write(self, address, data):

        self.data[address] = data

    def write_block(self, index, tag, entry):

        for block_off, word in entry.block.items():
            mem_address = (tag + index + block_off)
            mem_address = mem_address[-(self.address_size):]

            self.write(mem_address, word)

    def __str__(self):

        mem_viz = " INDEX     | DATA\n"

        for k, v in self.data.items():
            mem_viz += f"{k} | {hex(int(v, 2))}\n"

        return mem_viz

    def __getitem__(self, slice_key):

        sliced_mem = copy.deepcopy(self)
        new_data = dict(list(self.data.items())[slice_key])
        sliced_mem.data = new_data
        return sliced_mem
