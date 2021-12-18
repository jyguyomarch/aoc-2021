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

f = open('d18_snailfish/snailfish_input_test.txt','r')
lines = f.read().splitlines()

snail_number_list = []
for line in lines:
    snail_number = eval(line)
    print(snail_number)
    snail_number_list.append(snail_number)