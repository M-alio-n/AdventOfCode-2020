from string import ascii_lowercase

def count_yes_all(string):
    answ_by_person = string.split(" ")[:-1]
    true_false_lol = [[letter in answ for answ in answ_by_person] for letter in ascii_lowercase]
    return sum([all(answ_by_letter) for answ_by_letter in true_false_lol]) 


# initialize the first empty string and count variable
string = ""
count = 0
# load the file...
infile = open(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 6\input.txt").read().splitlines()
# ...line by line
for line in infile:
    if line != "":
        string = string + line + " "
    else:
        count += count_yes_all(string)
        string = ""
count += count_yes_all(string)
print(count)