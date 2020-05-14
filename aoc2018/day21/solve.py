from computer import Computer
import copy
import os
import re

program_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day21.txt'
with open(filename) as f:
    line = f.readline().strip()
    ip_ptr = int(line.split()[-1])

    for line in f:
        instruction = line.strip().split()
        for i in range(1, 4):
            instruction[i] = int(instruction[i])
        program_data.append(instruction)

# Part 1
comp = Computer(ip_ptr, [0, 0, 0, 0, 0, 0])
comp.set_program(copy.deepcopy(program_data))
print(comp.get_first_breakvalue())

# Part 2
comp = Computer(ip_ptr, [0, 0, 0, 0, 0, 0])
comp.set_program(copy.deepcopy(program_data))
print(comp.get_last_breakvalue())
