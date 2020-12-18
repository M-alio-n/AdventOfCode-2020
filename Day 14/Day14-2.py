from itertools import permutations
def num2bit(number):
    return '{0:036b}'.format(number)

def masking(mask, entry, number):
    global memory
    bit_entry = num2bit(entry)
    for cnt, mask_ind in enumerate(mask):
        if mask_ind == "X":
            tmp = list(bit_entry)
            tmp[cnt] = "X"
            bit_entry = "".join(tmp)
        elif mask_ind == "1":
            tmp = list(bit_entry)
            tmp[cnt] = "1"
            bit_entry = "".join(tmp)
    # This is a list which contains the indices of "X" within the mask
    positions_of_X = [ind for ind in range(len(bit_entry)) if list(bit_entry)[ind] == "X"]
    num_of_x = len(positions_of_X)
    
    # Iterate over the number of zeros that replace the Xs (all others are 1)
    for num_of_zeros in range(0, num_of_x + 1):
        str_of_bin = "0" * num_of_zeros + "1" * (num_of_x - num_of_zeros)
        # Uniquely get all combinations of binary string
        combis = set(permutations(str_of_bin))
        
        for combination in combis:
            tmp_entry_bin = bit_entry
            for replacement in list(combination):
                tmp_entry_bin = tmp_entry_bin.replace("X", replacement, 1)
            memory[int(tmp_entry_bin, 2)] = number


# set inputfilepath
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 14\input.txt"
# initialize list for the playfield
tasks = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        tasks.append(line)

memory = {}
mask = ""
entry = 0
count = 0
for task in tasks:
    if task[0:4] == "mask":
        mask = task[7:]
    elif task[0:3] == "mem":
        entry = int(task.split("[")[1].split("]")[0])
        number = int(task.split("= ")[1])
        masking(mask, entry, number)
    
    count += 1
   

final_sum = 0
for entry in memory:
    final_sum += memory[entry]
    
print(final_sum)
