#--- Day 11: Dumbo Octopus ---
#https://adventofcode.com/2021/day/11

import numpy as np

def flash(grid, row, column):
    max_row, max_col = grid.shape
    if grid[row][column] != float('inf'):
        grid[row][column] = float('inf')
        #energize neighbors
        if row - 1 >= 0:
            #top left
            if column - 1 >= 0:
                grid[row - 1][column - 1] += 1
                if grid[row - 1][column - 1] > 9:
                    flash(grid, row - 1, column - 1)
            #top middle
            grid[row - 1][column] += 1
            if grid[row - 1][column] > 9:
                flash(grid, row - 1, column)
            #top right
            if column + 1 < max_col:
                grid[row - 1][column + 1] += 1
                if grid[row - 1][column + 1] > 9:
                    flash(grid, row - 1, column + 1)
        if row + 1 < max_row:
            #bottom left
            if column - 1 >= 0:
                grid[row + 1][column - 1] += 1
                if grid[row + 1][column - 1] > 9:
                    flash(grid, row + 1, column - 1)
            #bottom middle
            grid[row + 1][column] += 1
            if grid[row + 1][column] > 9:
                flash(grid, row + 1, column)
            #bottom right
            if column + 1 < max_col:
                grid[row + 1][column + 1] += 1
                if grid[row + 1][column + 1] > 9:
                    flash(grid, row + 1, column + 1)
        #middle left
        if column - 1 >= 0:
            grid[row][column - 1] += 1
            if grid[row][column - 1] > 9:
                flash(grid, row, column - 1)
        #middle right
        if column + 1 < max_col:
            grid[row][column + 1] += 1
            if grid[row][column + 1] > 9:
                flash(grid, row, column + 1)

        
f = open('d11_octopus/octo_input.txt','r')
lines = f.read().splitlines()

octo_raw = []
for line in lines:
    octo_raw.append([float(val) for val in line])

octo_field = np.array(octo_raw)
rows, columns = octo_field.shape
flashes = 0
# 1000 steps
for step in range(400):
    #increase energy
    octo_field += 1
    
    #parse field and flash
    for col_idx in range(columns):
        for row_idx in range(rows):
            val = octo_field[row_idx][col_idx]
            if val > 9:
                flash(octo_field, row_idx, col_idx)

    #count flashed
    unique, counts = np.unique(octo_field, return_counts=True)
    if float('inf') in unique:
        flashes += counts[-1]
        
    #reset flashed
    octo_field = np.where(octo_field > 9, 0, octo_field)

    #verify if flash is synchronized accross all octopus
    if np.all((octo_field == 0)):
        print(f'Flashed synchronization at step: {step + 1}')

print(flashes)

# Sol 1: 1571
# Sol 2: 387