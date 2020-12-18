import numpy as np

# initialize the counter that counts the trees hit and the lines in the world
tree_count = 0
line_count = 0

# load the file...
infile = open(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 3\input.txt").read().splitlines()

# initialize the array that holds the geography
world = []
# ...line by line
for line in infile:
    world.append(line*60)
    line_count += 1

pos_x = 0
pos_y = 0
while pos_y < 323:
    print(r"pos_y {}, pos_x {}, value {}".format(pos_y, pos_x, world[pos_y][pos_x]))
    if world[pos_y][pos_x] == "#":
        tree_count += 1
    pos_y += 1
    pos_x += 3
print(tree_count)