class Computer():
    def __init__(self, ptr, regs):
        self.ip_reg = ptr
        self.inst_ptr = 0
        self.regs = regs
        self.op_map = {
            'addr': 0, 'addi': 1,
            'mulr': 2, 'muli': 3,
            'banr': 4, 'bani': 5,
            'borr': 6, 'bori': 7,
            'setr': 8, 'seti': 9,
            'gtir': 10, 'gtri': 11, 'gtrr': 12,
            'eqir': 13, 'eqri': 14, 'eqrr': 15,
        }
        self.program = []

    def set_program(self, program):
        self.inst_ptr = 0
        self.program = program

    def execute_program(self):
        while True:
            if self.inst_ptr < 0 or self.inst_ptr >= len(self.program):
                break

            self.execute_instruction(self.program[self.inst_ptr])

    def execute_instruction(self, instruction):
        opcode = self.op_map[instruction[0]]
        in_1 = instruction[1]
        in_2 = instruction[2]
        out = instruction[3]

        self.regs[self.ip_reg] = self.inst_ptr

        if opcode == 0:    # addr
            self.regs[out] = self.regs[in_1] + self.regs[in_2]
        elif opcode == 1:  # addi
            self.regs[out] = self.regs[in_1] + in_2
        elif opcode == 2:  # mulr
            self.regs[out] = self.regs[in_1] * self.regs[in_2]
        elif opcode == 3:  # muli
            self.regs[out] = self.regs[in_1] * in_2

        elif opcode == 4:  # banr
            self.regs[out] = self.regs[in_1] & self.regs[in_2]
        elif opcode == 5:  # bani
            self.regs[out] = self.regs[in_1] & in_2
        elif opcode == 6:  # borr
            self.regs[out] = self.regs[in_1] | self.regs[in_2]
        elif opcode == 7:  # bori
            self.regs[out] = self.regs[in_1] | in_2

        elif opcode == 8:  # setr
            self.regs[out] = self.regs[in_1]
        elif opcode == 9:  # seti
            self.regs[out] = in_1

        elif opcode == 10:  # gtir
            self.regs[out] = int(in_1 > self.regs[in_2])
        elif opcode == 11:  # gtri
            self.regs[out] = int(self.regs[in_1] > in_2)
        elif opcode == 12:  # gtrr
            self.regs[out] = int(self.regs[in_1] > self.regs[in_2])

        elif opcode == 13:  # eqir
            self.regs[out] = int(in_1 == self.regs[in_2])
        elif opcode == 14:  # eqri
            self.regs[out] = int(self.regs[in_1] == in_2)
        elif opcode == 15:  # eqrr
            self.regs[out] = int(self.regs[in_1] == self.regs[in_2])

        self.inst_ptr = self.regs[self.ip_reg]
        self.inst_ptr += 1
