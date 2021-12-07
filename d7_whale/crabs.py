#--- Day 7: The Treachery of Whales ---
#https://adventofcode.com/2021/day/7

# Get Data
f = open('d7_whale/crab_input.txt','r')
crabs = [int(pos) for pos in f.read().split(',')]

min_fuel = float('inf')
min_fuel_tri = float('inf')

# brute force going through all possibilities
for i in range(min(crabs), max(crabs)):
    fuel = 0
    fuel_tri = 0
    for crab in crabs:
        n = abs(crab - i)
        fuel += n
        fuel_tri += n*(n+1)/2
    min_fuel = min(min_fuel, fuel)
    min_fuel_tri = min(min_fuel_tri, fuel_tri)

print(min_fuel)
print(min_fuel_tri)

# Part 1: 347509
# Part 2: 98257206