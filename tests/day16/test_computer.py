from aoc2018.day16.computer import Computer
import unittest

class TestComputer(unittest.TestCase):
    def test_opcode_candidates_are_received(self):
        self.assertEqual(
            set([1, 2, 9]),
            Computer([3, 2, 1, 1]).get_opcode_candidates([9, 2, 1, 2], [3, 2, 2, 1])
        )
