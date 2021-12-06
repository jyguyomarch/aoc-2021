#--- Day 5: Hydrothermal Venture ---
#https://adventofcode.com/2021/day/5

import re
import matplotlib.pyplot as plt
import numpy as np

def draw_line(vmap, start, end):
    x1, y1 = start
    x2, y2 = end
    if x1 == x2 or y1 == y2:
        # consider straight lines
        if x1 == x2:
            if y2 > y1:
                for i in range(y2 - y1 + 1):
                    vmap[y1+i][x1] += 1
            if y1 > y2:
                for i in range(y1 - y2 + 1):
                    vmap[y1-i][x1] += 1
        if y1 == y2:
            if x2 > x1:
                for i in range(x2 - x1 + 1):
                    vmap[y1][x1+i] += 1
            if x1 > x2:
                for i in range(x1 - x2 + 1):
                    vmap[y1][x1-i] += 1
    else:
        # consider diagonals
        dx = 0
        dy = 0
        diag_range = 0
        if x1 < x2:
            dx = 1
            diag_range = x2 - x1
        else:
            dx = -1
            diag_range = x1 - x2
        if y1 < y2:
            dy = 1
        else:
            dy = -1
        for i in range(diag_range + 1):
            vmap[y1+(i*dy)][x1+(i*dx)] += 1

# Get data
f = open('d5_hydro_vents/squid_input.txt','r')
lines = f.read().splitlines()

# Process data to a list of tuples (x1, y1), (x2, y2)
vents_tuple = []
max_x = 0
max_y = 0
for line in lines:
    re_match = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line)
    x1, y1, x2, y2 = re_match.groups()
    max_x = max(max_x, int(x1), int(x2))
    max_y = max(max_y, int(y1), int(y2))
    vents_tuple.append(((int(x1), int(y1)), (int(x2), (int(y2)))))

# Create empty vent map of zeros
vent_map = np.zeros((max_y + 1, max_x + 1))

# Process vent lines
for from_end, to_end in vents_tuple:
    draw_line(vent_map, from_end, to_end)

#find the max
print(f'Hydrothermal Venture Danger count: {np.count_nonzero(vent_map >= 2)}')

plt.imshow(vent_map, cmap='hot', interpolation='nearest')
plt.show()

# Part 1: 8350
# Part 2: 19374