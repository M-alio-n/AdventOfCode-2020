def num2bit(number):
    return '{0:036b}'.format(number)

def masking(mask, number):
    masked = ""
    for mask_ind, num_ind in zip(mask, number):
        if mask_ind == "X":
            masked = masked + num_ind
        elif mask_ind == "0" or mask_ind == "1":
            masked = masked + mask_ind
    return masked

# set inputfilepath
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 14\input.txt"
# initialize list for the playfield
tasks = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        tasks.append(line)

memory = []
mask = ""
entry = 0
for task in tasks:
    if task[0:4] == "mask":
        mask = task[7:]
    elif task[0:3] == "mem":
        entry = int(task.split("[")[1].split("]")[0])
        number = int(task.split("= ")[1])
        while entry >= len(memory):
            memory.append("0"*36)
        memory[entry] = masking(mask, num2bit(number))

final_sum = 0
for space in memory:
    final_sum += int(space, 2)
print(final_sum)
