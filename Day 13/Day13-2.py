import math
import numpy as np

def get_prime_factors(number):
    # create an empty list and later I will
    # run a for loop with range() function using the append() method to add elements to the list.
    prime_factors = []

    # First get the number of two's that divide number
    # i.e the number of 2's that are in the factors
    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    # After the above while loop, when number has been
    # divided by all the 2's - so the number must be odd at this point
    # Otherwise it would be perfectly divisible by 2 another time
    # so now that its odd I can skip 2 ( i = i + 2) for each increment
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i


    # Here is the crucial part.
    # First quick refreshment on the two key mathematical conjectures of Prime factorization of any non-Prime number
    # Which is - 1. If n is not a prime number AT-LEAST one Prime factor would be less than sqrt(n)
    # And - 2. If n is not a prime number - There can be AT-MOST 1 prime factor of n greater than sqrt(n).
    # Like 7 is a prime-factor for 14 which is greater than sqrt(14)
    # But if the above loop DOES NOT go beyond square root of the initial n.
    # Then how does that greater than sqrt(n) prime-factor
    # will be captured in my prime factorization function.
    # ANS to that is - in my first for-loop I am dividing n with the prime number if that prime is a factor of n.
    # Meaning, after this first for-loop gets executed completely, the adjusted initial n should become
    # either 1 or greater than 1
    # And if n has NOT become 1 after the previous for-loop, that means that
    # The remaining n is that prime factor which is greater that the square root of initial n.
    # And that's why in the next part of my algorithm, I need to check whether n becomes 1 or not,
    if number > 2:
        prime_factors.append(int(number))

    return prime_factors

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

# set inputfilepath
filepath = r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 13\input.txt"
# initialize list for the playfield
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if cnt != 0:
            string = line
timestamps = string.split(",")

offsets = np.array([off for off in range(0, len(timestamps)) if timestamps[off] != "x"])
lines = np.array([int(timestamps[off]) for off in range(0, len(timestamps)) if timestamps[off] != "x"])





# Attempt using prime factors
# del_offset = offsets - offsets[np.argmax(lines)]
# print(lines)
# print(get_prime_factors(max(lines)))
# x = floor(100000000000000/max(lines))
x = 1
x = 163148000000

print(lines)
print(offsets)
pairs = []
del_offset = offsets - offsets[np.argmax(lines)]
for line_ind in range(0, len(lines)):
    print("Line {} has the offsets {}".format(lines[line_ind], offsets - offsets[line_ind]))
    for offset_ind in range(0, len(lines)):
        # offsets - offsets[line_ind]
        if lines[line_ind] == abs(offsets[offset_ind] - offsets[line_ind]):
            pairs.append([lines[line_ind], lines[offset_ind]])
            print("Line {} arrives with line {}".format(lines[line_ind], lines[offset_ind]))
print(pairs)

products = []
for line in lines:
    product = line
    for pair in pairs:
        if pair[1] == line:
            product = product * pair[0]
    products.append(product)
    print("Line {} multiples are of {}".format(line, product))

x = math.floor(100000000000000/max(products))
flag = 0
# while flag == 0:
while True:
    arrival_max = int(max(products)) * x
    arrivals = arrival_max + np.array([-13, -6, 0, 14, 19, 23, 29, 31, 72])
    if all(arrivals/lines == np.round(arrivals/lines)):
        print(arrivals[0])
        exit()
    x += 1
    
