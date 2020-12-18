def value_isvalid(number):
    global rules
    for rule_key in rules:
        if (number >= rules[rule_key][0] and number <= rules[rule_key][1]) or (number >= rules[rule_key][2] and number <= rules[rule_key][3]):
            return True
    return False

def ticket_isvalid(ticket_list):
    if all([value_isvalid(number) for number in ticket_list]):
        return True
    else:
        return False
            


# set inputfilepath
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 16\input.txt"
# initialize list for the playfield
tickets = []
rules = {}
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if cnt <= 19:   #19
            tmp_list = []
            for pair in line.split(":")[1].strip(" \n").split(" or "):
                for num in pair.split("-"):
                    tmp_list.append(int(num))
            rules[line.split(":")[0]] = tmp_list
        elif cnt == 22: #22
            my_ticket = [int(number) for number in line.strip("\n").split(",")]
        elif cnt >= 25: #25
            tickets.append([int(number) for number in line.strip("\n").split(",")])
count = 0
for ticket_list in tickets:
    for number in ticket_list:
        if not value_isvalid(number):
            count += number

print(count)

        