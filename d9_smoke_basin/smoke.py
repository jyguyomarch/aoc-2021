#--- Day 9: Smoke Basin ---
#https://adventofcode.com/2021/day/9

import numpy as np

f = open('d9_smoke_basin/smoke_input.txt','r')
lines = f.read().splitlines()

basin_raw = []
for line in lines:
    basin_raw.append([int(val) for val in line])

basin = np.array(basin_raw)
x, y = basin.shape

risk_levels = 0
for i in range(y):
    for j in range(x):
        val = basin[j][i]
        low_point = True
        if i > 0 and val >= basin[j][i-1]: low_point = False
        elif i < y - 1 and val >= basin[j][i+1]: low_point = False
        elif j > 0 and val >= basin[j-1][i]: low_point = False
        elif j < x - 1 and val >= basin[j+1][i]: low_point = False
        if low_point:
            risk_levels += val + 1

print(risk_levels)

# Sol Part 1: 607