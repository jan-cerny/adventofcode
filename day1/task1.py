#!/usr/bin/python3

import math

def count_fuel(mass):
    result = math.floor(mass / 3) - 2
    return result
    
sum = 0
with open("input", "r") as f:
    for line in f:
        mass = int(line)
        fuel = count_fuel(mass)
        sum += fuel
print(sum)