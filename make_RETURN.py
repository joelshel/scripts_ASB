#!usr/bin/env python3

with open("all_groEL_aln_aliview.fasta", "r") as f:
    lines = f.readlines()
with open("all_groEL_aln_aliview.fasta", "w") as f:
    count = 0
    for line in lines:
        if ">" in line and count != 0:
            f.write("\n")
        f.write(line)
        count += 1