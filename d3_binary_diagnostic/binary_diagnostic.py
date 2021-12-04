#--- Day 3: Binary Diagnostic ---
#https://adventofcode.com/2021/day/3

def calc_freq(bin_list):
    bits = [0 for i in range(len(bin_list[0]))]
    for bin in bin_list:
        index = 0
        for digit in bin:
            bits[index] += int(digit)
            index += 1
    return bits

f = open('d3_binary_diagnostic/binary_input.txt','r')
lines = f.read().splitlines()

bits = calc_freq(lines)
gamma_rate = epsilon_rate = ''
for freq in bits:
    if freq >= len(lines) / 2:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print(f'Gamma Rate: {gamma_rate} {int(gamma_rate,2)}')
print(f'Epsilon Rate: {epsilon_rate} {int(epsilon_rate,2)}')
print(f'Part 1 - Power Consumption: {int(gamma_rate,2) * int(epsilon_rate,2)}')

oxy_list = [x for x in lines]
co2_list = [x for x in lines]

index = 0
while len(oxy_list) > 1 or len(co2_list) > 1:
    # Oxy Reduction
    oxy_freq = calc_freq(oxy_list)
    if len(oxy_list) > 1:
        if oxy_freq[index] >= len(oxy_list) / 2:
            #1 more common
            oxy_list = [oxy for oxy in oxy_list if oxy[index] == '1']
        else:
            #0 more common
            oxy_list = [oxy for oxy in oxy_list if oxy[index] == '0']

    # CO2 Reduction
    co2_freq = calc_freq(co2_list)
    if len(co2_list) > 1:
        if co2_freq[index] >= len(co2_list) / 2:
            #1 more common
            co2_list = [co2 for co2 in co2_list if co2[index] == '0']
        else:
            #0 more common
            co2_list = [co2 for co2 in co2_list if co2[index] == '1']
    index += 1


print(f'Oxygen Generator Rating: {oxy_list[0]} {int(oxy_list[0],2)}')
print(f'CO2 scrubber rating: {co2_list[0]} {int(co2_list[0],2)}')
print(f'Part 2 - Life Support Rating: {int(oxy_list[0],2) * int(co2_list[0],2)}')

# Gamma Rate: 010111100100 1508
# Epsilon Rate: 101000011011 2587
# Part 1 - Power Consumption: 3901196
# Oxygen Generator Rating: 011001100111 1639
# CO2 scrubber rating: 101010000100 2692
# Part 2 - Life Support Rating: 4412188