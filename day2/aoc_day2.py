#!/usr/bin/python3

brute_val = 19690720

def initialize_intcode():
    with open("day2_input.txt", 'r') as f:
        intcode_str = f.read().strip()
        intcode = list(map(int, intcode_str.split(',')))
    return intcode

def calculate(intcode, val1, val2):
    intcode[1] = val1
    intcode[2] = val2
    eip = 0
    while True:
        arg1_pos = intcode[eip+1]
        arg2_pos = intcode[eip+2]
        out_pos = intcode[eip+3]
        if intcode[eip] == 1:
            intcode[out_pos] = intcode[arg1_pos] + intcode[arg2_pos]
        elif intcode[eip] == 2:
            intcode[out_pos] = intcode[arg1_pos] * intcode[arg2_pos]
        elif intcode[eip] == 99:
            break
        else:
            print("You broke it.")
        eip += 4

def bruteforce(val):
    intcode_orig = initialize_intcode()
    intcode = intcode_orig.copy()
    for noun in range(100):
        for verb in range(100):
            calculate(intcode, noun, verb)
            if intcode[0] == val:
                return noun, verb
            intcode = intcode_orig.copy()

intcode = initialize_intcode()
calculate(intcode, 12, 2)
noun, verb = bruteforce(brute_val)

print("Part 1: " + str(intcode[0]))
print("Part 2: " + str((100*noun)+verb))