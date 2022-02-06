from classes.cache import Cache
from classes.memory import PhysicalMemory

class MemorySystem:
    def __init__(self):

        self.memory_n_words = 1024
        self.cache_n_blocks = 64
        self.cache_block_size = 4
        self.cpu_address_size = 32
        self.cache = Cache(self.cache_n_blocks, self.cache_block_size)
        self.memory = PhysicalMemory(self.memory_n_words)

    def read(self, cpu_address, verb=True):

        word, status = self.cache.read(cpu_address, self.memory, verb)
        return word, status

    def write(self, cpu_address, data, verb=True):

        self.cache.write(cpu_address, data, self.memory, verb)
