def value_isvalid(number):
    global rules
    for rule_key in rules:
        if (number >= rules[rule_key][0] and number <= rules[rule_key][1]) or (number >= rules[rule_key][2] and number <= rules[rule_key][3]):
            return True
    return False

def rule_check(number, rule_key):
    global rules
    # print("Checking rule {} for number {}".format(rule_key, number))
    if (number >= rules[rule_key][0] and number <= rules[rule_key][1]) or (number >= rules[rule_key][2] and number <= rules[rule_key][3]):
        # print("Found true")
        return True
    # print("Found false")
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
for index in range(len(tickets)-1, -1, -1):
    if not ticket_isvalid(tickets[index]):
        del tickets[index]

rule_pos = {}
for key in rules:
    rule_pos[key] = [num for num in range(0,len(rules))]

for ticket in tickets:
    for cnt, number in enumerate(ticket):
        for rule in rule_pos:
            if not rule_check(number, rule):
                try:
                    rule_pos[rule].remove(cnt)
                except:
                    print("Nothing to remove")

new_rule_pos = {}
count = 1
# while any([len(rule_pos[key]) > 1 for key in rule_pos]):
    # print(rule_pos)
while any([len(rule_pos[rule]) >= 1 for rule in rule_pos]):
    for rule in rules:
        if len(rule_pos[rule]) == 1:
            new_rule_pos[rule] = rule_pos[rule][0]
            for rule_key in rule_pos:
                try:
                    rule_pos[rule_key].remove(new_rule_pos[rule])
                except:
                    print("Nothing to remove")

answer = 1
for rule in new_rule_pos:
    if "departure" in rule:
        answer *= my_ticket[new_rule_pos[rule]]
print(answer)