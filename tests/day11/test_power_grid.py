from aoc2018.day11.power_grid import PowerGrid
import unittest

class TestPowerGrid(unittest.TestCase):
    def test_cell_value_is_calculated(self):
        self.assertEqual(4, PowerGrid(8).calculate_cell(3, 5))
        self.assertEqual(-5, PowerGrid(57).calculate_cell(122, 79))
        self.assertEqual(0, PowerGrid(39).calculate_cell(217, 196))
        self.assertEqual(4, PowerGrid(71).calculate_cell(101, 153))

    def test_max_fixed_square_gets_found(self):
        self.assertEqual(
            {'x': 33, 'y': 45, 'power': 29, 'size': 3},
            PowerGrid(18).find_max_square(3)
        )
        self.assertEqual(
            {'x': 21, 'y': 61, 'power': 30, 'size': 3},
            PowerGrid(42).find_max_square(3)
        )

    def test_max_any_square_gets_found(self):
        self.assertEqual(
            {'x': 90, 'y': 269, 'power': 113, 'size': 16},
            PowerGrid(18).find_max_square()
        )
