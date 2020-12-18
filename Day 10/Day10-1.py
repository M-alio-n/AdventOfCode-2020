import numpy as np
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 10\input.txt"
list_of_numbers = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        list_of_numbers.append(int(line))

list_of_numbers = np.insert(list_of_numbers, 0, 0)

result = sorted(list_of_numbers)
differences = np.diff(result)

differences = np.append(differences, 3)

print(result)

count_1 = 0
count_3 = 0
for ind in range(0, len(differences)):
    if differences[ind] == 1:
        count_1 += 1
        continue
    elif differences[ind] == 3:
        count_3 += 1
print(count_1)
print(count_3)

print(count_1*count_3)