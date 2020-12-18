import numpy as np

filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 10\input.txt"
list_of_numbers = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        list_of_numbers.append(int(line))

def count_arrangements(number_list):
    if len(number_list) == 1 or len(number_list) == 2:
        return 1
    elif len(number_list) == 3:
        return 2
    elif len(number_list) == 4:
        return 4
    elif len(number_list) == 5:
        return 7

list_of_numbers = np.insert(list_of_numbers, 0, 0)

list_of_numbers = sorted(list_of_numbers)
differences = np.diff(list_of_numbers)

differences = np.append(differences, 3)

diff_3 = [0]
print(type(diff_3))
for ind in range(0, len(differences)):
    if differences[ind] == 3:
        diff_3.append(ind+1)

sublists = [list_of_numbers[diff_3[index]:diff_3[index+1]] for index in range(0, len(diff_3)-1)]
count = 1
for sublist in sublists:
    count *= count_arrangements(sublist)
print(count)
