import numpy as np
from itertools import cycle
# define a function that handles the turns
def move_ship(action, argument):
    global position_change, facing, face
    if action == "N":
        position_change += [0, argument]
        return
    if action == "S":
        position_change += [0, -argument]
        return
    if action == "E":
        position_change += [argument, 0]
        return
    if action == "W":
        position_change += [-argument, 0]
        return
    if action == "F":
        position_change += facing * argument
        return
    if action == "L":
#        print("Facing {} on position {}".format(facing, position_change))
#        print("Turning {}, {} with face {} turn to {}".format(action, argument, face, face - int(argument/90)))
        face = (face - int(argument/90)) % 4
        facing = directions[face]
#        print("Facing {} on position {}".format(facing, position_change, face))
        return
    if action == "R":
#        print("Turning {}, {} with face {} turn to {}".format(action, argument, face, (face + int(argument/90)) % 4))
        face = (face + int(argument/90)) % 4
        facing = directions[face]
        return




# set inputfilepath
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 12\input.txt"
# initialize list for the playfield
actions = []
arguments = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        actions.append(line[0])
        arguments.append(int(line[1:].strip("\n")))

# defina a list of directions   E, S, W, N
directions = [np.array([1, 0]), np.array([0, -1]), np.array([-1,0]), np.array([0, 1])]
# position at start
start = np.array([0, 0])
# how does the ship move
position_change = np.array([0, 0])
# where does the ship face? [1,0] = E, [-1,0] = W, [0, 1] = N, [0, -1] = S
face = 0
facing = directions[face]

# run the commands
for act, arg in zip(actions, arguments):
    move_ship(act, arg)
    print("Facing {} on position {}".format(facing, position_change))
print(abs(position_change[0]) + abs(position_change[1]))