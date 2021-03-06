fin = open(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 6\testinput.txt")

# myinput = fin.readlines()

def groups(gfile):
    current_group = []
    for line in gfile:
        line=line.strip()
        if line == '':
            yield current_group
            current_group = []
            continue
        current_group.append(line)
    if current_group != []:
        yield current_group

yes_sum = 0

for group in groups(fin):
    for i,member in enumerate(group):
        if i == 0:
            common = set(member)
        else:
            common = common.intersection(set(member))
    yes_num = len(common)
    print(group,common,yes_num)
    yes_sum += yes_num

print(yes_sum)