numbers = [6,13,1,15,2,0]
# numbers = [2,1,3]

# initialize:
count = 1
memory = {}
last_number = 0
for number in numbers:
    last_number = number
    memory[str(number)] = [count, 0]
    count += 1

while count <= 30000000:
    entry = memory[str(last_number)]
    if entry[1] == 0:
        next_number = 0
    else:
        next_number = entry[0] - entry[1]
    try:
        test = memory[str(next_number)]
        memory[str(next_number)] = [count, memory[str(next_number)][0]]
    except:
        memory[str(next_number)] = [count, 0]
    # print("I say {}".format(next_number))
    last_number = next_number
    count += 1
print(last_number)