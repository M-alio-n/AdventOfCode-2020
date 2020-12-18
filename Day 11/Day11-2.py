def find_neighours(field, idx_1, idx_2):
    neighbours = []
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
    for direct in dirs:
        ind_1 = direct[0] + idx_1
        ind_2 = direct[1] + idx_2
        while ind_1 > 0 and ind_1 < len(field) and ind_2 > 0 and ind_2 < len(field[0]):
            if field[ind_1][ind_2] == "L" or field[ind_1][ind_2] == "#":
                neighbours.append(field[ind_1][ind_2])
                break
            ind_1 += direct[0]
            ind_2 += direct[1]
    return neighbours


# set inputfilepath
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 11\input.txt"
# initialize list for the playfield
field = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        field.append("." + line.strip("\n") + ".")
# "zeropad" the field
field.insert(0, "." * len(field[0]))
field.append("." * len(field[0]))

prev_field = []
# go through all entries in the list
while field != prev_field:
    prev_field = field.copy()
    tmp_field = field.copy()
    for indx_1 in range(1, len(field)-1):
        for indx_2 in range(1, len(field[0])-1):
            if field[indx_1][indx_2] != ".":
                neighbours = find_neighours(field, indx_1, indx_2)
                if sum([letter == "#" for letter in neighbours]) == 0 and field[indx_1][indx_2] == "L":
                    tmp = list(tmp_field[indx_1])
                    tmp[indx_2] = "#"
                    tmp_field[indx_1] = ''.join(tmp)
                elif sum([letter == "#" for letter in neighbours]) >= 5 and field[indx_1][indx_2] == "#":
                    tmp = list(tmp_field[indx_1])
                    tmp[indx_2] = "L"
                    tmp_field[indx_1] = ''.join(tmp)

    field = tmp_field.copy()

print(sum([field[idx_1][idx_2] == "#" for idx_1 in range(1, len(field)-1) for idx_2 in range(1, len(field[0])-1)]))
