print("I'm in")
from numpy import loadtxt
from sys import exit

input_values = loadtxt(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 1\input.txt")

for num1 in input_values:
    for num2 in input_values:
        for num3 in input_values:
            if num1+num2+num3 == 2020:
                print(num1*num2*num3)
                exit()