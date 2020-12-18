from math import ceil
# set inputfilepath
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 13\input.txt"
# initialize list for the playfield
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if cnt == 0:
            min_timestamp = int(line.strip("\n"))
        else:
            string = line
timestamps = string.split(",")

min_deps = [[ceil(min_timestamp/int(stamp))*int(stamp), int(stamp)] for stamp in timestamps if stamp != "x"]
print(min(min_deps))
print(min(min_deps)[1] * (min(min_deps)[0] - min_timestamp))