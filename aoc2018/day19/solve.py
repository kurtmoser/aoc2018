from computer import Computer
import os
import re

program_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day19.txt'
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
comp.set_program(program_data)
comp.execute_program()
print(comp.regs[0])

# Part 2
comp = Computer(ip_ptr, [1, 0, 0, 0, 0, 0])
comp.set_program(program_data)

while True:
    comp.execute_instruction(comp.program[comp.inst_ptr])

    # Once we reack instruction 1 we know that setup is complete and register
    # 2 contains value we need to solve
    if comp.inst_ptr == 1:
        break

print(sum([i for i in range(1, comp.regs[2] + 1) if comp.regs[2] % i == 0]))
