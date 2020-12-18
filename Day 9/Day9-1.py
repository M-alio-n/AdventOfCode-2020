def check_sum_of_two(prev_list, new_num):
    for index_1 in range(len(prev_list)-2):
        for index_2 in range(len(prev_list)-1,index_1,-1):
            if prev_list[index_1] + prev_list[index_2] == new_num:
                return True
    return False

filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 9\input.txt"
list_of_numbers = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        list_of_numbers.append(int(line))

preamb_length = 25
sublist = list_of_numbers[0:preamb_length]
for new_num_idx in range(preamb_length, len(list_of_numbers[preamb_length:])):
    print(sublist)
    print(list_of_numbers[new_num_idx])
    if not check_sum_of_two(sublist, list_of_numbers[new_num_idx]):
        print("The winner is: {}".format(list_of_numbers[new_num_idx]))
        exit()
    # delete first entry
    sublist.pop(0)
    # append next value
    sublist.append(list_of_numbers[new_num_idx])
print("Exit regularly")