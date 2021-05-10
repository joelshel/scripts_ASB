#!/usr/bin/env python3

# files = []

# for c in range(2,31):
#     files.append(f"anaplasma{c}.fasta")

try:
# for file in files:
    with open("all_groEL.fasta", "r") as f:
        lines = f.readlines()
    with open("all_groEL.fasta", "w") as f:
        for line in lines:
            f.write(line)
            if line == ">Anaplasma centrale/Israel\n":
                break
            print(line, end='')
except FileNotFoundError:
    print("We cannot access to the file!")
    