#--- Day 11: Dumbo Octopus ---
#https://adventofcode.com/2021/day/11

import numpy as np

f = open('d11_octopus/octo_input_test.txt','r')
lines = f.read().splitlines()

octo_raw = []
for line in lines:
    octo_raw.append([int(val) for val in line])

octo_field = np.array(octo_raw)

# 1000 steps
for step in range(100):
    #increase energy
    octo_field += 1
    
    #reset flashed
    octo_field = np.where(octo_field > 9, 0, octo_field)

print(octo_field)