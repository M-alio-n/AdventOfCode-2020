from string import ascii_lowercase

def count_yes_questions(string):
    return sum([letter in string for letter in ascii_lowercase])


# initialize the first empty string and count variable
string = ""
count = 0
# load the file...
infile = open(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 6\input.txt").read().splitlines()
# ...line by line
for line in infile:
    if line != "":
        string = string + line
    else:
        count += count_yes_questions(string)
        string = ""
print(count)