#--- Day 13: Transparent Origami ---
#https://adventofcode.com/2021/day/13

f = open('d13_origami/origami_input_test.txt','r')
lines = f.read().splitlines()

import numpy as np

dots_list = []
fold_instructions = []
max_x = max_y = 0
for line in lines:
    if len(line) != 0:
        if line[0:11] == 'fold along ':
            fold_instructions.append((line[11], int(line[13:])))
        else:
            dot = [int(val) for val in line.split(',')]
            if dot[0] > max_x: max_x = dot[0]
            if dot[1] > max_y: max_y = dot[1]
            dots_list.append((dot[0], dot[1]))


paper = np.zeros(shape=(max_y + 1, max_x + 1))

for x,y in dots_list:
    paper[y][x] = 1

first_fold = 0
for axis, index in fold_instructions:
    if axis == 'y':
        #fold horizontally
        paper_1 = paper[0:index]
        paper_2 = np.flip(paper[index+1:],0)
        paper = paper_1 + paper_2
    else:
        #fold vertivally
        paper = np.rot90(paper, k=1, axes=(0,1))
        paper_1 = paper[0:index]
        paper_2 = np.flip(paper[index+1:],0)
        paper = paper_1 + paper_2
        paper = np.rot90(paper, k=1, axes=(1,0))
    if first_fold == 0:
        first_fold = np.count_nonzero(paper)
    print(paper)

print(first_fold)
