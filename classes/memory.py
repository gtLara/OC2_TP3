from math import log

class PhysicalMemory:

    def __init__(self, n_words=1024, word_size=32):

        self.data = {}
        n_bits_index = int(log(n_words, 2))
