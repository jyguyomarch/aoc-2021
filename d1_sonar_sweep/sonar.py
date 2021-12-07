#--- Day 1: Sonar Sweep ---
#https://adventofcode.com/2021/day/1

import sys

lines = sys.stdin.read().splitlines()
if len(lines) == 0:
    f = open('d1_sonar_sweep/input.txt','r')
    lines = f.readlines()
depth_readings = [int(depth) for depth in lines]

#PART 1: compare sliding window of depth 2
depth_pair = zip(depth_readings, depth_readings[1:])
depth_increase = 0
for depth1, depth2 in depth_pair:
    if depth2 > depth1:
        depth_increase += 1
print('AOC Day 1 - Sonar Sweep - Part 1: ' + str(depth_increase))

#PART 2: compare sliding window of depth 3
depth_trio = zip(depth_readings, depth_readings[1:], depth_readings[2:])
depth_trio_sums = []
for trio in depth_trio:
    depth_trio_sums.append(sum(list(trio)))
depth_sums_pairs = zip(depth_trio_sums, depth_trio_sums[1:])
depth_increase = 0
for depth1, depth2 in depth_sums_pairs:
    if depth2 > depth1:
        depth_increase += 1
print(f'AOC Day 1 - Sonar Sweep - Part 2: {depth_increase}')

#SOL: 1616, 1645