import sys
import os
# os.system('color') # to get colored printing working on windows
from termcolor import colored
from utils.entry import get_line_info, generate_result_file, get_input_file_lines
from classes.system import MemorySystem

memory_system = MemorySystem()

try: # tenta acessar primeiro argumento passado a programa como nome de arquivo de entrada

    input_file = sys.argv[1]

except IndexError:
    print(colored("Nome de arquivo faltando!", "red"))
    print("Execute python test.py <nome_arquivo_teste>")
    exit()

lines = get_input_file_lines(input_file)

output_log = []
output_lines = ""

for line in lines:

    operation, address, data = get_line_info(line)

    if operation == '1': # write case

        memory_system.write(address, data) # actual write operation

        # logging stuff for result.txt

        output_log.append("WRITES")
        output_lines += line.strip()+" W\n"

        # printing operation as mnemonic

        print(f"mem[{address}] = {hex(int(data, 2))}")

    else: # read case

        word, status = memory_system.read(address) # actual read operation

        # logging stuff for result.txt

        output_log.append("READS")

        if status == "H":
            output_log.append("HITS")
        else:
            output_log.append("MISSES")

        output_lines += line.strip()+f" {status}\n"

        # printing operation as mnemonic

        print(f"value in mem[{address}] is {hex(int(word, 2))}")

generate_result_file(output_log, output_lines)
