#!/usr/bin/python3

class Program:
    def __init__(self, intcode, input_val):
        self.intcode = intcode[:]
        self.halted = False
        self.input_val = input_val

    def get_param(self, mode, val):
        if mode == 0:
            return self.intcode[val]
        else:
            return val

    def run(self):
        pc = 0
        while self.halted == False:
            instruction = self.intcode[pc]
            opcode = instruction % 100          # Get the rightmost 2 digits
            mode1 = (instruction // 100) % 10   # Get the middle digit
            mode2 = (instruction // 1000) % 10  # Get the second digit
            mode3 = instruction // 10000        # Get the first digit
            if opcode == 1:
                self.intcode[self.intcode[pc+3]] = (self.get_param(mode1, self.intcode[pc+1])) + (self.get_param(mode2, self.intcode[pc+2]))
                pc += 4
            elif opcode == 2:
                self.intcode[self.intcode[pc+3]] = (self.get_param(mode1, self.intcode[pc+1])) * (self.get_param(mode2, self.intcode[pc+2]))
                pc += 4
            elif opcode == 3:
                self.intcode[self.intcode[pc+1]] = self.input_val
                pc += 2
            elif opcode == 4:
                print(self.intcode[self.intcode[pc+1]])
                pc += 2
            elif opcode == 5:
                if self.get_param(mode1, self.intcode[pc+1]) != 0:
                    pc = self.get_param(mode2, self.intcode[pc+2])
                else:
                    pc += 3
            elif opcode == 6:
                if self.get_param(mode1, self.intcode[pc+1]) == 0:
                    pc = self.get_param(mode2, self.intcode[pc+2])
                else:
                    pc += 3
            elif opcode == 7:
                if self.get_param(mode1, self.intcode[pc+1]) < self.get_param(mode2, self.intcode[pc+2]):
                    self.intcode[self.intcode[pc+3]] = 1
                    pc += 4
                else:
                    self.intcode[self.intcode[pc+3]] = 0
                    pc += 4
            elif opcode == 8:
                if self.get_param(mode1, self.intcode[pc+1]) == self.get_param(mode2, self.intcode[pc+2]):
                    self.intcode[self.intcode[pc+3]] = 1
                    pc += 4
                else:
                    self.intcode[self.intcode[pc+3]] = 0
                    pc += 4
            elif opcode == 99:
                self.halted = True
                break
            else:
                print("It broke.")

def get_intcode():
    with open("day5_input.txt", 'r') as f:
        intcode_str = f.read().strip()
        intcode = list(map(int, intcode_str.split(',')))
    return intcode

print("Part 1: ")
program = Program(get_intcode(), 1)
program.run()

print("Part 2: ")
program = Program(get_intcode(), 5)
program.run()
