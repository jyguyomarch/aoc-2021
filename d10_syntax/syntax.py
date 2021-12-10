#--- Day 10: Syntax Scoring ---
#https://adventofcode.com/2021/day/10

f = open('d10_syntax/syntax_input.txt','r')
lines = f.read().splitlines()

opening_dict = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

closing_dict = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

lifo = []
scoring = 0
for line in lines:
    for c in line:
        if c in opening_dict.keys():
            lifo.append(c)
        if c in closing_dict.keys():
            last_in = lifo.pop()
            if c != opening_dict[last_in]:
                scoring += closing_dict[c]
                break

print(scoring)