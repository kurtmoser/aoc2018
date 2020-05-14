from aoc2018.day19.computer import Computer
import unittest

class TestComputer(unittest.TestCase):
    def test_instruction_pointer_is_supported(self):
        comp = Computer(0, [0, 0, 0, 0, 0, 0])
        comp.set_program([
            ['seti', 5, 0, 1],
            ['seti', 6, 0, 2],
            ['addi', 0, 1, 0],
            ['addr', 1, 2, 3],
            ['setr', 1, 0, 0],
            ['seti', 8, 0, 4],
            ['seti', 9, 0, 5],
        ])
        comp.execute_program()
        self.assertGreaterEqual(comp.inst_ptr, len(comp.program))
        self.assertEqual([6, 5, 6, 0, 0, 9], comp.regs)
