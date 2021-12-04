#--- Day 2: Dive! ---
#https://adventofcode.com/2021/day/2

f = open('d2_dive/dive_input.txt','r')
lines = f.readlines()
commands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]
#commands = []
#for line in lines:
#    command = line.split(' ')
#    commands.append((command[0], int(command[1])))

h_position = 0
depth = 0
aim = 0
h_position_2 = 0
depth_2 = 0
for step, value in commands:
    if step == 'forward':
        h_position += value
        h_position_2 += value
        depth_2 += aim * value
    if step == 'down':
        depth += value
        aim += value
    if step == 'up':
        depth -= value
        aim -= value

print(f'Part 1 - Horizontal Position: {h_position}, Depth: {depth}')
print(f'Part 1 - Solution: {h_position * depth}')

print(f'Part 2 - Horizontal Position: {h_position_2}, Depth: {depth_2}, Aim: {aim}')
print(f'Part 2 - Solution: {h_position_2 * depth_2}')

#Part 1 - Horizontal Position: 2007, Depth: 747
#Part 1 - Solution: 1499229
#Part 2 - Horizontal Position: 2007, Depth: 668080, Aim: 747
#Part 2 - Solution: 1340836560