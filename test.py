import sys
import os
# os.system('color') # to get colored printing working on windows
from termcolor import colored
from collections import Counter
from classes.system import MemorySystem

try:
    fn = sys.argv[1]
except IndexError:
    print(colored("Nome de arquivo faltando!", "red"))
    print("Execute python test.py <nome_arquivo_teste>")
    exit()

memory_system = MemorySystem()

try:
    with open(f"{fn}", "r") as input_file:
        lines = input_file.readlines()
except FileNotFoundError:
    err = f"O arquivo fornecido {fn} não existe ou está com o caminho errado"
    print(colored(err, "red"))
    exit()

output_file = open(f"result.txt", "w+")
output_log = []
output_lines = ""

for line in lines:

    split_line = line.strip().split(" ")

    if int(split_line[1]): # write case

        address = format(int(split_line[0]), "032b")
        data = split_line[2]

        memory_system.write(address, data)

        output_log.append("WRITES")
        output_lines += line.strip()+" W\n"
        print(f"mem[{address}] = {hex(int(data, 2))}")

    else: # read case

        address = format(int(split_line[0]), "032b")

        word, status = memory_system.read(address)

        output_log.append("READS")

        if status == "H":
            output_log.append("HITS")
        else:
            output_log.append("MISSES")

        output_lines += line.strip()+f" {status}\n"
        print(f"value in mem[{address}] is {hex(int(word, 2))}")

output_log = Counter(output_log)

for observation, count in output_log.items():
    output_file.write(f"{observation}:{count}\n")

hit_rate = output_log["HITS"]/output_log["READS"]
miss_rate = output_log["MISSES"]/output_log["READS"]

output_file.write(f"HIT RATE:{hit_rate}\n")
output_file.write(f"MISS RATE:{miss_rate}\n\n")
output_file.write(output_lines)

output_file.close()
