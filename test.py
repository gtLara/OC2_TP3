import sys
from classes.cache import Cache
from classes.memory import PhysicalMemory

try:
    fn = sys.argv[1]
except IndexError:
    print("Nome de arquivo faltando!")
    print("Execute python test.py <nome_arquivo_teste>")
    exit()

mem = PhysicalMemory()
cache = Cache()

print(cache[0:7])
print(mem[0:26])

with open(f"{fn}", "r") as input_file:
    lines = input_file.readlines()

output_file = open(f"{fn}_output", "w+")

for line in lines:

    split_line = line.strip().split(" ")

    if int(split_line[1]): # write case
        output_file.write(line.strip()+" W\n")
        address = format(int(split_line[0]), "032b")
        data = split_line[2]
        print(f"mem[{address}] = {hex(int(data, 2))}")
        cache.write(address, data, mem)
        print(cache[0:7])
        print(mem[0:26])

    else: # read case

        output_file.write(line.strip()+" R\n")
        address = format(int(split_line[0]), "032b")
        word = cache.read(address, mem)
        print(f"value in mem[{address}] is {hex(int(word, 2))}")
        print(cache[0:7])
        print(mem[0:26])

output_file.close()
