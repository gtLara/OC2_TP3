with open("testes/simple_test", "r") as file:
    lines = file.readlines()

lines = [line.strip().split(" ") for line in lines]

for line in lines:

    if int(line[1]): # write case
        address = line[0]
        data = line[2]

        # memory_system.write(data, address)

    else: # read case

        address = line[0]

        # value = memory_system.read(address)
