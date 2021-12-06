#--- Day 6: Lanternfish ---
#https://adventofcode.com/2021/day/6

# Get Data
f = open('d6_lanternfish/fish_input.txt','r')
lanternfishs = [int(fish) for fish in f.read().split(',')]

# for i in range(0):
#     new_fishies = 0
#     for j in range(len(lanternfishs)):
#         if lanternfishs[j] == 0:
#             lanternfishs[j] = 6
#             new_fishies += 1
#         else:
#             lanternfishs[j] -= 1
#     lanternfishs += [ 8 for x in range(new_fishies)]

# print(f'Lanternfish pop: {len(lanternfishs)}')

fish_counter = [ 0 for x in range(9)]
for x in lanternfishs:
    fish_counter[int(x)] += 1

for tick in range(80):
    for i in range(8):
        if i == 0:
            new_fishies = fish_counter[i]
        fish_counter[i] = fish_counter[i+1]
    # new babies
    fish_counter[8] = new_fishies
    # reset 0 fish to 6
    fish_counter[6] += new_fishies

print(f'Lanternfish pop: {sum(fish_counter)}')

# Sol Part 1 - Lanternfish pop: 349549
# Sol Part 2 - Lanternfish pop: 1589590444365