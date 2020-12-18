def count_bag_in_bag(inpt_bag_dict, inpt_num_dict, key):
    position = 0
    count = 0
    for contained in inpt_bag_dict[key]:
        count += inpt_num_dict[key][position] * count_bag_in_bag(inpt_bag_dict, inpt_num_dict, contained) + inpt_num_dict[key][position]
        position += 1
    print("Returning {} for {}".format(count, key))
    return count

# open file
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 7\input.txt"
# initialize the dictionary
bag_dict = {}
number_dict = {}
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
        contains_list_numbers = []
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
                contains_list_numbers.append(int(substring[0]))
            bag_dict[new_key] = contains_list
            number_dict[new_key] = contains_list_numbers

count = count_bag_in_bag(bag_dict, number_dict, "shiny gold")
print(count)