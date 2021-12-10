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

incomplete_dict = {
    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4
}

incomplete_stacks = []
scoring = 0
for line in lines:
    corrupted = False
    lifo = []
    for c in line:
        if c in opening_dict.keys():
            lifo.append(c)
        if c in closing_dict.keys():
            last_in = lifo.pop()
            if c != opening_dict[last_in]:
                scoring += closing_dict[c]
                corrupted = True
                break
    if not corrupted:
        incomplete_stacks.append(lifo)

print(scoring)

# Score the incomplete stacks
incomplete_scores = []
for stack in incomplete_stacks:
    stack.reverse()
    score = 0
    for c in stack:
        score *= 5
        score += incomplete_dict[c]
    incomplete_scores.append(score)

incomplete_scores.sort()
print(incomplete_scores[int(len(incomplete_scores) / 2)])

# Sol Part 1: 311895