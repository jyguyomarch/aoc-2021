#--- Day 9: Smoke Basin ---
#https://adventofcode.com/2021/day/9

import numpy as np
from collections import Counter

from numpy.core.fromnumeric import sort

def is_low_point(grid, row, column):
    row_max, col_max = grid.shape
    value = grid[row][column]
    if column > 0 and value >= grid[row][column-1]:
        return False
    elif column < col_max - 1 and value >= grid[row][column+1]:
        return False
    elif row > 0 and value >= grid[row-1][column]:
        return False
    elif row < row_max - 1 and value >= grid[row+1][column]:
        return False
    return True

def mark_and_check_adjacents(grid, row, column, marker):
    if grid[row][column] > 8:
        return
    row_max, col_max = grid.shape
    value = grid[row][column]
    grid[row][column] = marker
    if column > 0 and value < grid[row][column-1]:
        mark_and_check_adjacents(grid, row, column - 1, marker)
    if column < col_max - 1 and value < grid[row][column+1]:
        mark_and_check_adjacents(grid, row, column + 1, marker)
    if row > 0 and value < grid[row-1][column]:
        mark_and_check_adjacents(grid, row - 1, column, marker)
    if row < row_max - 1 and value < grid[row+1][column]:
        mark_and_check_adjacents(grid, row + 1, column, marker)

f = open('d9_smoke_basin/smoke_input.txt','r')
lines = f.read().splitlines()

basin_raw = []
for line in lines:
    basin_raw.append([int(val) for val in line])

basin = np.array(basin_raw)
rows, columns = basin.shape

risk_levels = 0
for col_idx in range(columns):
    for row_idx in range(rows):
        val = basin[row_idx][col_idx]
        if is_low_point(basin, row_idx, col_idx):
            risk_levels += val + 1

print(risk_levels)

# Sol Part 1: 607

# part 2

marker = 10
# loop through the matrix
for col_idx in range(columns):
    for row_idx in range(rows):
        # find a low point
        if basin[row_idx][col_idx] < 9 and is_low_point(basin, row_idx, col_idx):
            # mark all adjacents recursively
            mark_and_check_adjacents(basin, row_idx, col_idx, marker)
            marker += 1

unique, counts = np.unique(basin, return_counts=True)
largest_basins = dict(zip(unique, counts))
largest_basins.pop(9)
largest_basins_list = list(largest_basins.values())
largest_basins_list.sort()
print(np.prod(largest_basins_list[-3:]))
    
