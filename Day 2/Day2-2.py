# import the xor operator
from operator import xor

# initialize the counter that counts the occurences of valid passwords
count = 0

# load the file...
infile = open(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 2\input.txt").read().splitlines()

# ...line by line
for line in infile:
    # split the line into the different parts
    res = line.split(' ')
    letter = res[1][0]
    password = res[2]
    upper = int(res[0].split('-')[1])
    lower = int(res[0].split('-')[0])
    # check if the password of the current line is valid
    if xor(password[lower-1] == letter, password[upper-1] == letter):
        # if so increase the count by 1
        count += 1
print(count)