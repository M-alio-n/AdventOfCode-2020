import numpy as np
from itertools import cycle
# define a function that handles the turns
def move_ship(action, argument):
    global position_change, facing, face, waypoint
    if action == "N":
        waypoint += np.array([0, argument])
        return
    if action == "S":
        waypoint += np.array([0, -argument])
        return
    if action == "E":
        waypoint += np.array([argument, 0])
        return
    if action == "W":
        waypoint += np.array([-argument, 0])
        return
    if action == "F":
        print(type(waypoint))
        print(argument)
        position_change += np.array(waypoint * argument)
        return
    if action == "L":
        if argument/90 == 2:
            waypoint = -waypoint
        if argument/90 == 1:
            waypoint = np.array([-waypoint[1], waypoint[0]])
        if argument/90 == 3:
            waypoint = np.array([waypoint[1], -waypoint[0]])
        if argument/90 == 4:
            print("We have a rebel here!")
        return
    if action == "R":
        if argument/90 == 2:
            waypoint = -waypoint
        if argument/90 == 1:
            waypoint = np.array([waypoint[1], -waypoint[0]])
        if argument/90 == 3:
            waypoint = np.array([-waypoint[1], waypoint[0]])
        if argument/90 == 4:
            print("We have a rebel here!")
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

waypoint = np.array([10, 1])
# run the commands
for act, arg in zip(actions, arguments):
    move_ship(act, arg)
    print("Facing {} on position {}".format(facing, position_change))
print(abs(position_change[0]) + abs(position_change[1]))