#--- Day 5: Hydrothermal Venture ---
#https://adventofcode.com/2021/day/5

import re
import numpy as np

def draw_line(vmap, start, end):
    x1, y1 = start
    x2, y2 = end
    if x1 == x2 or y1 == y2:
        #only consider straight lines
        vmap[y1][x1] += 1
        vmap[y2][x2] += 1

# Get data
f = open('d5_hydro_vents/vents_input_test.txt','r')
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

print(vents_tuple)
print(f'Max x: {max_x}, Max y: {max_y}')

# Create empty vent map of zeros
vent_map = np.zeros((max_y + 1, max_x + 1))

# Process vent lines
for from_end, to_end in vents_tuple:
    draw_line(vent_map, from_end, to_end)

#find the max
print(vent_map)

danger_count = np.count_nonzero(vent_map >= 2)

print(f'Danger count: {danger_count}')
