
def run_operation(string):
    if string[0:3] == "nop":
        return [1, 0]
    elif string[0:3] == "acc":
        return [1, int(string[4:])]
    elif string[0:3] == "jmp":
        return [int(string[4:]), 0]

def history_repeats(history):
    if len(history) == 1:
        return False
    for entry in range(len(history)):
        for entry_2 in range(entry+1, len(history)):
            if history[entry] == history[entry_2]:
                return True
    return False
 
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 8\input.txt"
program = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        program.append(line.replace("\n",""))

position = 0
history = [0]
accumulator = 0
while not history_repeats(history):
    [del_pos, del_acc] = run_operation(program[position])
    accumulator += del_acc
    position += del_pos
    history.append(position)
print(accumulator)