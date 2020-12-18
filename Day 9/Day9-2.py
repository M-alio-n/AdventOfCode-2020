filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 9\input.txt"
list_of_numbers = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        list_of_numbers.append(int(line))


magic_number = 675280050
#magic_number = 127
for start in range(0, len(list_of_numbers)):
    more = 0
    while sum(list_of_numbers[start:start+more]) <= magic_number:
        if sum(list_of_numbers[start:start+more]) == magic_number:
            print("The winner is {} + {} = {}".format(min(list_of_numbers[start:start+more]), max(list_of_numbers[start:start+more]), min(list_of_numbers[start:start+more])+ max(list_of_numbers[start:start+more])))
            exit()
        more += 1