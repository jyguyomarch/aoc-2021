#--- Day 6: Lanternfish ---
#https://adventofcode.com/2021/day/7

# Get Data
f = open('d7_whale/crab_input.txt','r')
crabs = [int(pos) for pos in f.read().split(',')]

min_fuel = None
min_fuel_tri = None

# brute force going through all possibilities
for i in range(max(crabs)):
    fuel = 0
    fuel_tri = 0
    for crab in crabs:
        n = abs(crab - i)
        fuel += n
        fuel_tri += n*(n+1)/2
    if min_fuel is None or fuel < min_fuel:
        min_fuel = fuel
    if min_fuel_tri is None or fuel_tri <  min_fuel_tri:
        min_fuel_tri = fuel_tri

print(min_fuel)
print(min_fuel_tri)

# Part 1: 347509
# Part 2: 98257206