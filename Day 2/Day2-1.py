infile = open(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 2\input.txt").read().splitlines()

count = 0
for line in infile:
    res = line.split(' ')
    letter = res[1][0]
    password = res[2]
    upper = int(res[0].split('-')[1])
    lower = int(res[0].split('-')[0])
    if lower <= password.count(letter) <= upper:
        count += 1
print(count)