#!/usr/bin/env python3

try:
# for file in files:
    with open("all_groEL_aln_aliview.fasta", "r") as f:
        lines = f.readlines()
    with open("all_groEL_aln_aliview.fasta", "w") as f:
        for line in lines:
            if len(line) < 60:
                f.write(line)
            else:
                parts = len(line)//60+1
                caracteres = 0
                for c in range(1, parts+1):
                    if c != parts:
                        f.write(line[caracteres:(caracteres+60)]+"\n")
                    else:
                        f.write(line[caracteres:])
                    caracteres += 60
                    
            print(line, end='')
except FileNotFoundError:
    print("We cannot access to the file!")
    