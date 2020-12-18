import numpy as np
from math import ceil

def get_neighbours(X_coord, Y_coord, Z_coord):
    global array
    # print(X_coord-1)
    # print(X_coord+1)
    # print(array[X_coord-1:X_coord+2, Y_coord-1:Y_coord+2, Z_coord-1:Z_coord+2])
    # print(sum(sum(sum(array[X_coord-1:X_coord+2, Y_coord-1:Y_coord+2, Z_coord-1:Z_coord+2]))) - array[X_coord, Y_coord, Z_coord])
    return sum(sum(sum(array[X_coord-1:X_coord+2, Y_coord-1:Y_coord+2, Z_coord-1:Z_coord+2]))) - array[X_coord, Y_coord, Z_coord]


# set inputfilepath
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 17\input.txt"
# initialize list for the playfield
image = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        image.append(line.strip("\n"))
# number of cycles to run
cycles = 6
# initialize array with zeros
array = np.zeros((len(image) + 2*(cycles + 1), len(image) + 2*(cycles + 1), len(image) + 2*(cycles + 1)))
for cnt, line in enumerate(image):
    tmp = []
    for char in line:
        if char == ".":
            tmp.append(0)
        else:
            tmp.append(1)
    array[ceil(len(array)/2) - ceil(len(line)/2), cnt + ceil(len(array)/2) - ceil(len(line)/2), ceil(len(array)/2) - ceil(len(line)/2):ceil(len(array)/2) - ceil(len(line)/2) + len(image)] = np.array(tmp)

for cycle in range(cycles):
    tmp = np.copy(array)
    for find in range(0,2):
        coords = np.where(array == find)
        for cube in range(len(coords[0])):
            if any([coords[dim][cube] == 0 for dim in range(3)]) or any([coords[dim][cube] == len(array)-1 for dim in range(3)]):
                continue
            if find == 1:
                if get_neighbours(coords[0][cube], coords[1][cube], coords[2][cube]) == 2 or get_neighbours(coords[0][cube], coords[1][cube], coords[2][cube]) == 3:
                    print(coords[0][cube], coords[1][cube], coords[2][cube])
                    print("Stayin' alife")
                else:
                    tmp[coords[0][cube], coords[1][cube], coords[2][cube]] = 0
                    print(coords[0][cube], coords[1][cube], coords[2][cube])
                    print("Killing living cell")
            if find == 0:
                if get_neighbours(coords[0][cube], coords[1][cube], coords[2][cube]) == 3:
                    tmp[coords[0][cube], coords[1][cube], coords[2][cube]] = 1
                    print(coords[0][cube], coords[1][cube], coords[2][cube])
                    print("Populating dead cell")
    array = np.copy(tmp)
print(sum(sum(sum(array))))
        