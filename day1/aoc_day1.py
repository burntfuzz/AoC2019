#!/usr/bin/python3

import sys

with open(sys.argv[1], 'r') as f:
	weights = [int(l) for l in f.readlines()]

fuel_sum = sum((w//3-2) for w in weights)

additional_fuel = 0
for w in weights:
    w = w//3-2
    while w > 0:
        additional_fuel += w
        w = w//3-2

print("Part 1: " + str(fuel_sum))        
print("Part 2: " + str(additional_fuel))