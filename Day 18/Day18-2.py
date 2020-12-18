import numpy as np
import fnmatch

def calculate_expression(string):
    both_indices = [index for index, char in enumerate(string) if char in "+*"]
    plus_indices = [index for index, char in enumerate(string) if char in "+"]
    mult_indices = [index for index, char in enumerate(string) if char in "*"]
    if len(both_indices) == 1:
        substring = string[0:]
    elif len(plus_indices) > 0:
        try:
            next_sign = both_indices[both_indices.index(plus_indices[0])+1]
        except:
            next_sign = len(string)
        if both_indices.index(plus_indices[0])-1 >= 0:
            prev_sign = both_indices[both_indices.index(plus_indices[0])-1] + 1
        else:
            prev_sign = 0
        substring = string[prev_sign:next_sign]
    else:
        substring = string[0:both_indices[1]]

    if "+" in substring:
        value = str(int(substring.split("+")[0]) + int(substring.split("+")[1]))
    elif "*" in substring:
        value = str(int(substring.split("*")[0]) * int(substring.split("*")[1]))


    if len(both_indices) == 1:
        return value
    else:
        return calculate_expression(string.replace(substring, value, 1))

def calculate_line(string):
    if string.find("(") != -1:
        substring_w_par = string[string.rfind("("):]
        substring_w_par = substring_w_par[:substring_w_par.find(")")+1]
        substring_in_par = substring_w_par[1:substring_w_par.find(")")]
        string = string.replace(substring_w_par, calculate_expression(substring_in_par))
        return calculate_line(string)
    if string.find("(") == -1:
        return calculate_expression(string)

# set inputfilepath
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 18\input.txt"
# initialize list for the playfield
calculations = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        calculations.append(line.strip("\n").replace(' ', ''))

res_list = []
for calculation in calculations:
    res_list.append(int(calculate_line(calculation)))
print(sum(res_list))