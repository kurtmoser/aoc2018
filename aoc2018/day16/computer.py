class Computer():
    def __init__(self, regs):
        self.regs = regs

    def exec(self, ops, force_opcode=None):
        if force_opcode != None:
            opcode = force_opcode
        else:
            opcode = ops[0]

        if opcode == 0:    # addr
            self.regs[ops[3]] = self.regs[ops[1]] + self.regs[ops[2]]
        elif opcode == 1:  # addi
            self.regs[ops[3]] = self.regs[ops[1]] + ops[2]
        elif opcode == 2:  # mulr
            self.regs[ops[3]] = self.regs[ops[1]] * self.regs[ops[2]]
        elif opcode == 3:  # muli
            self.regs[ops[3]] = self.regs[ops[1]] * ops[2]

        elif opcode == 4:  # banr
            self.regs[ops[3]] = self.regs[ops[1]] & self.regs[ops[2]]
        elif opcode == 5:  # bani
            self.regs[ops[3]] = self.regs[ops[1]] & ops[2]
        elif opcode == 6:  # borr
            self.regs[ops[3]] = self.regs[ops[1]] | self.regs[ops[2]]
        elif opcode == 7:  # bori
            self.regs[ops[3]] = self.regs[ops[1]] | ops[2]

        elif opcode == 8:  # setr
            self.regs[ops[3]] = self.regs[ops[1]]
        elif opcode == 9:  # seti
            self.regs[ops[3]] = ops[1]

        elif opcode == 10:  # gtir
            self.regs[ops[3]] = int(ops[1] > self.regs[ops[2]])
        elif opcode == 11:  # gtri
            self.regs[ops[3]] = int(self.regs[ops[1]] > ops[2])
        elif opcode == 12:  # gtrr
            self.regs[ops[3]] = int(self.regs[ops[1]] > self.regs[ops[2]])

        elif opcode == 13:  # eqir
            self.regs[ops[3]] = int(ops[1] == self.regs[ops[2]])
        elif opcode == 14:  # eqri
            self.regs[ops[3]] = int(self.regs[ops[1]] == ops[2])
        elif opcode == 15:  # eqrr
            self.regs[ops[3]] = int(self.regs[ops[1]] == self.regs[ops[2]])

    def get_opcode_candidates(self, instruction, expected_output):
        original_regs = self.regs.copy()

        suitable_opcodes = set()

        for opcode in range(16):
            self.regs = original_regs.copy()
            self.exec(instruction, opcode)

            if self.regs == expected_output:
                suitable_opcodes.add(opcode)

        return suitable_opcodes

    def decode_opcodes(self, opcode_candidates):
        decoded_opcodes = {}

        for i in range(16):
            for j, candidates in opcode_candidates.copy().items():
                if len(candidates) == 1:
                    decoded_opcodes[j] = list(candidates)[0]
                    del(opcode_candidates[j])
                    [opcode_candidates[k].discard(list(candidates)[0]) for k in opcode_candidates]

        return decoded_opcodes
