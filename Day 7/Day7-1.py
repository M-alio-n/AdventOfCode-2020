def check_if_gold(inpt_dict, key):
    Flag = False
    for contained in inpt_dict[key]:
        if contained == "shiny gold" or Flag == True:
            Flag = True
            break
        else:
            Flag = check_if_gold(inpt_dict, contained)
    return Flag
MeineListe = []
# open file
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 7\inputJonas.txt"
# initialize the dictionary
bag_dict = {}
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        # create a new entry in the dict that contains the bags described in this line
        # and a list of bags that can go in there
        # get the new key
        new_key = line.split(" bag")[0]
        # get the remainder of the line
        remainder = line.split("contain ")[1:]
        # initialize the list that will be attributed to the new key
        contains_list = []
        if new_key != "shiny gold":
            if remainder[0][0:14] == "no other bags.":
                bag_dict[new_key] = []
            else:
                remainder = remainder[0].split(" bag")
                for substring in remainder[:-1]:
                    if substring[0:3] == "s, ":
                        substring = substring[3:]
                    elif substring[0:2] == ", ":
                        substring = substring[2:]
                    # in this line we remove the information about numbers, this might be needed in part 2!
                    contains_list.append(substring[2:])
                bag_dict[new_key] = contains_list

print(bag_dict)

count = 0
for key in bag_dict:
    if check_if_gold(bag_dict, key):
        count += 1
print(count)