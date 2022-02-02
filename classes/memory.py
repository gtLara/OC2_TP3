from utils import create_storage
import random
from math import log

def create_random_word(size=32):

    word = ""
    for i in range(size):
        word += str(random.randint(0, 1))

    return word

class PhysicalMemory:

    def __init__(self, n_words=1024, word_size=32, random=True):

        self.address_size = int(log(n_words, 2))

        if random:
            self.data = create_storage(n_words,
                                       initial_data=create_random_word)
        else:
            self.data = create_storage(n_words)

    def read(self, address):

        word = self.data[address]
        return word

    def write(self, address, data):

        self.data[address] = data