from classes.utils import create_storage, create_random_word, int_2_padded_bin
from math import log

class PhysicalMemory:

    def __init__(self, n_words=1024, word_size=32, random=True):

        self.n_words = n_words
        self.address_size = int(log(n_words, 2))

        if random:
            self.data = create_storage(n_words,
                                       init_data=create_random_word)
        else:
            self.data = create_storage(n_words)

    def read(self, address, spread=4): # TODO: review spread policy

        assert len(address) == self.address_size

        words = create_storage(spread)

        for k, key in enumerate(words.keys()):

            word_address = int(address, 2) + k

            assert word_address < self.n_words

            word_address = int_2_padded_bin(word_address, self.address_size)

            words[key] = self.data[word_address]

        return words

    def write(self, address, data):

        self.data[address] = data

    def __str__(self):

        mem_viz = " INDEX     | DATA\n"

        for k, v in self.data.items():
            mem_viz += f"{k} | {hex(int(v, 2))}\n"

        return mem_viz
