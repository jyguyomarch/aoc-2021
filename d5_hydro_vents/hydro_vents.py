#--- Day 5: Hydrothermal Venture ---
#https://adventofcode.com/2021/day/5

import re

# Get data
f = open('d5_hydro_vents/vents_input_test.txt','r')
lines = f.read().splitlines()

vents_tuple = []
for line in lines:
    re_match = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line)
    x1, y1, x2, y2 = re_match.groups()
    vents_tuple.append(((int(x1), int(y1)), (int(x2), (int(y2)))))

print(vents_tuple)