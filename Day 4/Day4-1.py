import numpy as np
# initialize the counter of valid passports
count = 0
# initialize an empty string that will save all information of the passport
string = ""
# initialize an array of required substrings
substrings = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
# load the file...
infile = open(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 4\input.txt").read().splitlines()
# ...line by line
for line in infile:
    if line != "":
        string = string + line + " "
    else:
        print(string)
        if all([substring in string for substring in substrings]):
            count += 1
        string = ""

if all([substring in string for substring in substrings]):
    count += 1
string = ""
print(count)