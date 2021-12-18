#--- Day 11: Passage Pathing ---
#https://adventofcode.com/2021/day/12

from collections import defaultdict, deque

def explore(connections, revisit_small):
    counter = 0
    stack = deque([("start", set(["start"]), False)])
    while stack:
        cave, seen, visited = stack.popleft()
        if cave == "end":
            counter += 1
            continue
        for cave_dest in connections[cave]:
            if not cave_dest in seen:
                seen_cave_dest = set(seen)
                if cave_dest.islower():
                    seen_cave_dest.add(cave_dest)
                stack.append((cave_dest, seen_cave_dest, visited))
            elif cave_dest in seen and not visited and cave_dest not in ["start", "end"] and revisit_small:
                stack.append((cave_dest, seen, True))
    return counter

f = open('d12_passage/path_input.txt','r')
lines = f.read().splitlines()

#dict of all the paths, both ways
connections = defaultdict(list)
for line in lines:
    c1, c2 = line.split('-')
    connections[c1].append(c2)
    connections[c2].append(c1)

part1 = explore(connections, False)
part2 = explore(connections, True)

print(f'Solution Part 1: {part1}')
print(f'Solution Part 2: {part2}')

# Part 1: 3761
# Part 2: 99138