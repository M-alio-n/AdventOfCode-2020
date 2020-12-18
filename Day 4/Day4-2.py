import numpy as np
import re
# import the xor operator
from operator import xor


# Define a function that will check if all passport entries in a string are correct
def check_validity(string):
    # initialize an array of required substrings
    substrings = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    entries = re.split(':| ', string)
    Types = ""
    temp_count = []
    for entry_no in range(0, len(entries)-1, 2):
        Types = Types + entries[entry_no]
    if all([substring in Types for substring in substrings]):
        for entry_no in range(0, len(entries)-1, 2):
            temp_count.append(check_all(entries[entry_no+1], entries[entry_no]))
        if all(temp_count):
            return 1
        else:
            return 0
    else:
        return 0

def check_all(string, entry):
    if entry == "byr":
        return check_byr(string)
    elif entry == "iyr":
        return check_iyr(string)
    elif entry == "eyr":
        return check_eyr(string)
    elif entry == "hgt":
        return check_hgt(string)
    elif entry == "hcl":
        return check_hcl(string)
    elif entry == "ecl":
        return check_ecl(string)
    elif entry == "pid":
        return check_pid(string)
    elif entry == "cid":
        return check_cid(string)


def check_byr(string):
    try:
        if 1920 <= int(string) <= 2002:
            return 1
        else:
            return 0
    except ValueError:
        return 0

def check_iyr(string):
    try:
        if 2010 <= int(string) <= 2020:
            return 1
        else:
            return 0
    except ValueError:
        return 0

def check_eyr(string):
    try:
        if 2020 <= int(string) <= 2030:
            return 1
        else:
            return 0
    except ValueError:
        return 0

def check_hgt(string):
    if string[-2:] == "cm":
        try:
            if 150 <= int(string[0:-2]) <= 193:
                return 1
            else:
                return 0
        except ValueError:
            return 0
    elif string[-2:] == "in":
        try:
            if 59 <= int(string[0:-2]) <= 76:
                return 1
            else:
                return 0
        except ValueError:
            return 0
    else:
        return 0

def check_hcl(string):
    if string[0] == "#" and len(string[1:]) == 6:
        if all([letter in "1234567890abcdef" for letter in string[1:]]):
            return 1
        else:
           return 0
    else:
        return 0

def check_ecl(string):
    if xor(string == "amb", xor(string == "blu", xor(string == "brn", xor(string == "gry", xor(string == "grn", xor(string == "hzl",  string == "oth")))))):
        return 1
    else:
        return 0

def check_pid(string):
    if len(string) == 9:
        try:
            int(string)
            return 1
        except ValueError:
            return 0
    else:
        return 0

def check_cid(string):
    return 1





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
        if check_validity(string):
            count += 1
        string = ""

if check_validity(string):
    count += 1
string = ""
print(count)