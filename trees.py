#!/usr/bin/env python3

import toytree
import toyplot
import toyplot.svg
from toytree.TreeParser import NewickError

outgroups = []
print("Insert input file") #in mrbayes format.")
in_file = input("> ")
out_file = in_file.split(".")[0]

print("Insert outgroups. ([N] to quit)")
while True:
    outgroup = input("> ")
    if outgroup in "Nn":
        break
    outgroups.append(outgroup)


try:
    in_file = open(in_file, "r")
    tree = ""
    for line in in_file:
        tree += line
    try:
        tre = toytree.tree(tree)

    except NewickError:
        tre = toytree.tree(tree, tree_format=10)

    if outgroups != []:
        rtre = tre.root(outgroups)
    try:
        # canvas, axes, mark = rtre.draw(width=1000, height=1000)
        canvas, axes, mark = rtre.draw(node_labels='support', node_sizes=15, width=1000, height=1000)
    except NameError:
        # canvas, axes, mark = tre.draw(width=1000, height=1000)
        canvas, axes, mark = tre.draw(node_labels='support', node_sizes=15, width=1000, height=1000)
    toyplot.svg.render(canvas, out_file + ".svg")
    print("Tree drawed successfully.")
except FileNotFoundError:
    print("We cannot find the file.")
    print("Verify if the file name is correct or if you insert the correct path.")
