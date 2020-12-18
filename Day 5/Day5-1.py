import math as m

# load the file...
infile = open(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 5\input.txt").read().splitlines()

def get_seat_ID(string):
    counter = 0
    upper_row = 127
    lower_row = 0
    upper_col = 7
    lower_col = 0
    for letter in string:
        if letter == "F":
            upper_row = upper_row - m.ceil((upper_row-lower_row)/2)
        elif letter == "B":
            lower_row = lower_row + m.ceil((upper_row-lower_row)/2)
        if letter == "L":
            upper_col = upper_col - m.ceil((upper_col-lower_col)/2)
        elif letter == "R":
            lower_col = lower_col + m.ceil((upper_col-lower_col)/2)
    return lower_row*8+lower_col

        


highest_ID = 0
for line in infile:
    if get_seat_ID(line) > highest_ID:
        highest_ID = get_seat_ID(line)
print(highest_ID)