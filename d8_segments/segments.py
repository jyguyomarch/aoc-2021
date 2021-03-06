#--- Day 8: Seven Segment Search ---
#https://adventofcode.com/2021/day/8

from collections import Counter

def common_seg(sig, pattern):
    count = 0
    for char in sig:
        if char in pattern: count += 1
    return count

f = open('d8_segments/segments_input.txt','r')
lines = f.read().splitlines()
journal = []
for log in lines:
    tmplog = log.split(' | ') 
    journal.append( (tmplog[0], tmplog[1]) )

# count 1, 4, 7, 8
l_freq = Counter()
for entry in journal:
    sig_pat, digits = entry
    # lengths: 2 -> 1, 3 -> 7, 4 -> 4, 7 -> 8
    l_freq.update([len(d) for d in digits.split(" ")])

print(f"Digits with unique patterns: {l_freq[2] + l_freq[3] + l_freq[4] + l_freq[7]}")

total = 0
for entry in journal:
    sig_pat, digits = entry
    for signal in sig_pat.split(" "):
        if len(signal) == 2: pat_ones = signal
        elif len(signal) == 4: pat_fours = signal
        elif len(signal) == 3: pat_sevens = signal
        elif len(signal) == 7: pat_eights = signal
    output = ''
    for d in digits.split(" "):
        if len(d) == 2: output += '1'
        elif len(d) == 4: output += '4'
        elif len(d) == 3: output += '7'
        elif len(d) == 7: output += '8'
        elif len(d) == 5:
            if common_seg(d, pat_ones) == 2: output += '3'
            elif common_seg(d, pat_fours) == 3: output += '5'
            else: output += '2'
        elif len(d) == 6:
            if common_seg(d, pat_fours) == 4: output += '9'
            elif common_seg(d, pat_sevens) == 3: output += '0'
            else:output += '6'
    total += int(output)

print(f'Total: {total}')