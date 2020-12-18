from numpy import loadtxt
from sys import exit

input_values = loadtxt(r"C:\Users\Jan\Documents\Python Scripts\AdventOfCode 2020\Day 1\input.txt")

lower_half=input_values[input_values < 2020/2]
upper_half=input_values[input_values > 2020/2]

for num1 in lower_half:
    for num2 in upper_half:
        if num1+num2 == 2020:
            print(num1*num2)
            exit()