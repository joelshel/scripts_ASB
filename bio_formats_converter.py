#!/usr/bin/env python3

from Bio import SeqIO

def converter(input_extension='fasta', output_extension='nexus'):
    print("-"*10, f"CONVERTOR FROM {input_extension.upper()} TO {output_extension.upper()}", "-"*10)

    while True:
        print("Type the file name what do you want to convert.")
        file = input("> ")
        file = file.split(".")[0]
        try:
            sequences = SeqIO.convert(f"{file}.{input_extension}", f"{input_extension}", f"{file}.{output_extension}", f"{output_extension}", "DNA")
        except FileNotFoundError:
            print("Error, file not found, verify if the file name is correct!")
            break

        print("Conversion executed successfully!")
        continue_ = input("Do you want to continue to convert files? [Y] or [N]")
        if continue_[0] in 'nN':
            break
    print("Exiting program.")

if __name__ == '__main__':
    converter()