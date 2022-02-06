import sys
from classes.system import MemorySystem

try:
    fn = sys.argv[1]
except IndexError:
    print("Nome de arquivo faltando!")
    print("Execute python test.py <nome_arquivo_teste>")
    exit()

memory_system = MemorySystem()

with open(f"{fn}", "r") as input_file:
    lines = input_file.readlines()

output_file = open(f"{fn}_output", "w+")
output_file.write("\n"*7)

for line in lines:

    split_line = line.strip().split(" ")

    if int(split_line[1]): # write case

        address = format(int(split_line[0]), "032b")
        data = split_line[2]

        memory_system.write(address, data)

        output_file.write(line.strip()+" W\n")
        print(f"mem[{address}] = {hex(int(data, 2))}")

    else: # read case

        address = format(int(split_line[0]), "032b")

        word, status = memory_system.read(address)

        output_file.write(line.strip()+f" {status}\n")
        print(f"value in mem[{address}] is {hex(int(word, 2))}")

output_file.close()
