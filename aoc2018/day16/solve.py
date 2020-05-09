from computer import Computer
import os
import re

sample_data = []
program_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day16.txt'
with open(filename) as f:
    while True:
        res = re.search(r'^Before: \[(\d+), (\d+), (\d+), (\d+)\]$', f.readline().strip())

        if res:
            before_state = list(map(int, res.groups()))

            res = re.search(r'^(\d+) (\d+) (\d+) (\d+)$', f.readline().strip())
            instruction = list(map(int, res.groups()))

            res = re.search(r'^After:  \[(\d+), (\d+), (\d+), (\d+)\]$', f.readline().strip())
            after_state = list(map(int, res.groups()))

            blankline = f.readline()

            sample_data.append({
                'bef': before_state,
                'inst': instruction,
                'aft': after_state,
            })
        else:
            break

    blankline = f.readline()

    for line in f:
        res = re.search(r'^(\d+) (\d+) (\d+) (\d+)$', line)
        program_data.append(list(map(int, res.groups())))

# Part 1
print(sum(len(Computer(data['bef']).get_opcode_candidates(data['inst'], data['aft'])) >= 3 for data in sample_data))

# Part 2
opcode_candidates = {i: set() for i in range(16)}
for data in sample_data:
    candidates = Computer(data['bef']).get_opcode_candidates(data['inst'], data['aft'])
    opcode_candidates[data['inst'][0]].update(candidates)

comp = Computer([0, 0, 0, 0])
decoded_opcodes = comp.decode_opcodes(opcode_candidates)

[comp.exec(instruction, decoded_opcodes[instruction[0]]) for instruction in program_data]

print(comp.regs[0])
