import numpy as np

# initialize the counter that counts the trees hit and the lines in the world

line_count = 0
tree_counts = []
# load the file...
infile = open(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 3\input.txt").read().splitlines()

# initialize the array that holds the geography
world = []
# ...line by line
for line in infile:
    world.append(line*100)
    line_count += 1

slope_x = [1,3,5,7,1]
slope_y = [1,1,1,1,2]

for slope_no in range(5):
    print (slope_no)
    pos_x = 0
    pos_y = 0
    tree_count = 0
    while pos_y < 323:
        if world[pos_y][pos_x] == "#":
            tree_count += 1
        pos_y += slope_y[slope_no]
        pos_x += slope_x[slope_no]
    print(tree_count)
    tree_counts.append(tree_count)
print(tree_counts)
print(np.prod(tree_counts))