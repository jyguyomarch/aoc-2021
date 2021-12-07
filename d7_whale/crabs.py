#--- Day 7: The Treachery of Whales ---
#https://adventofcode.com/2021/day/7

import statistics

# Get Data
f = open('d7_whale/crab_input_test.txt','r')
crabs = [int(pos) for pos in f.read().split(',')]

# Part 1: use the median
med = statistics.median(crabs)
min_fuel = sum([abs(crab_position - med) for crab_position in crabs])
print(f'Part 1: Crab position and fuel: {med}, {min_fuel}')

# Part 2: brute force going through all possibilities with quick exit
min_fuel_tri = float('inf')
best_position = float('inf')
for i in range(min(crabs), max(crabs)):
    fuel_tri = 0
    for crab in crabs:
        n = abs(crab - i)
        fuel_tri += n*(n+1)/2
        if fuel_tri > min_fuel:
            exit
    if fuel_tri < min_fuel_tri:
        min_fuel_tri = fuel_tri
        best_position = i

print(f'Part 2: Crab position and fuel: {best_position}, {min_fuel_tri}')

# Part 1: 347509
# Part 2: 98257206