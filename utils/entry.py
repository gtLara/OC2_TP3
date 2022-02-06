from collections import Counter
from termcolor import colored

def get_input_file_lines(fn):

    try:

        with open(f"{fn}", "r") as input_file:
            lines = input_file.readlines()

    except FileNotFoundError:
        err = f"O arquivo fornecido {fn} não existe ou está com o caminho errado"
        print(colored(err, "red"))
        exit()

    return lines

def get_line_info(line):

    split_line = line.strip().split(" ")
    address = format(int(split_line[0]), "032b")
    operation = split_line[1]

    if operation == "1":
        data = split_line[2]
    else:
        data = None

    return operation, address, data

def generate_result_file(output_log, output_lines):

    output_log = Counter(output_log)
    hit_rate = output_log["HITS"]/output_log["READS"]
    miss_rate = output_log["MISSES"]/output_log["READS"]

    with open(f"result.txt", "w+") as output_file:

        for observation, count in output_log.items():
            output_file.write(f"{observation}:{count}\n")

        output_file.write(f"HIT RATE:{hit_rate}\n")
        output_file.write(f"MISS RATE:{miss_rate}\n\n")
        output_file.write(output_lines)
