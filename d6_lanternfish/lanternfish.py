#--- Day 6: Lanternfish ---
#https://adventofcode.com/2021/day/6

# Get Data
f = open('d6_lanternfish/fish_input_test.txt','r')
lanternfishs = [int(fish) for fish in f.read().split(',')]

print(lanternfishs)