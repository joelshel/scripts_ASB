#!/usr/bin/env python3

import sys
import re
from multiprocessing import Pool
from time import time

def read_file(name_file):
    """Function to read a fasta file.

    Args:
        name_file (str): The name of the fasta file.

    Returns:
        list of str: A list with all the lines of the file.
    """
    try:
        with open(name_file, "r") as fasta:
            lines = fasta.readlines()
            return lines
    except FileNotFoundError as e:
        print(f"Got a {e.__class__}.")
        print(f"Can't find the file '{e.filename}'.")

def make_sequence_list(lines):
    """A function to filter the sequence names and to make a list of strings.
    where each string its the entire sequence.

    Args:
        lines (list of str): A list with all the lines of the file.

    Returns:
        list of str: A list without sequence names and each sequence separate.
    """
    sequences = list()
    for line in lines:
        if line.startswith(">"):
            try:
                sequences.append(sequence)
            except UnboundLocalError:
                pass
            sequence = ''
        else:
            sequence += line.strip().upper()
    sequences.append(sequence)
    return sequences

def get_exons(sequence):
    """A function which returns the sequence if it has a exon, else returns a empty string.

    Args:
        sequence (str): A fasta sequence (without sequence name).

    Returns:
        str: Sequence if it has a exon else a empty string.
    """
    exons = re.search(r"(((...)*ATG)(...)*?)((TAG|TAA|TGA))", sequence)
    try:
        exonstr = exons.group()
    except AttributeError:
        exonstr = ''
    return exonstr


if __name__ == "__main__":
    start = time()
    pool = Pool()
    lines = read_file(sys.argv[1])
    sequences = make_sequence_list(lines)
    exons = list(pool.map(get_exons, sequences))
    exons = [exon for exon in exons if exon != '']
    pool.map(print, exons)
    print(len(sequences))
    print(len(exons))
    end = time()
    print(end-start)