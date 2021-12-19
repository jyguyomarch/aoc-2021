#--- Day 18: Snailfish ---
#https://adventofcode.com/2021/day/18

def snail_add(left, right):
    return [left, right]

def snail_reduce(snail_number):
    pass

def snail_explode(snail_number):
    pass

def snail_split(snail_number):
    pass

def magnitude(snail_number):
    if type(snail_number) == int:
        return snail_number
    return 3 * magnitude(snail_number[0]) + 2 * magnitude(snail_number[1])

f = open('d18_snailfish/snailfish_input_test.txt','r')
lines = f.read().splitlines()

snail_number_list = []
added_snail = []
for i in range(len(lines) - 1):
    if len(added_snail) == 0:
        added_snail = eval(lines[i])
    added_snail = snail_add(added_snail, eval(lines[i+1])) 

# test magnitude
assert magnitude([[1,2],[[3,4],5]]) == 143
assert magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
assert magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445
assert magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488
    