from aoc2018.day17.water_system import WaterSystem
import unittest

class TestWaterSystem(unittest.TestCase):
    def setUp(self):
        self.water_system = WaterSystem([
            'x=495, y=2..7',
            'y=7, x=495..501',
            'x=501, y=3..7',
            'x=498, y=2..4',
            'x=506, y=1..2',
            'x=498, y=10..13',
            'x=504, y=10..13',
            'y=13, x=498..504',
        ])

    def test_water_count_is_calculated(self):
        self.water_system.run_until_overflow()
        self.assertEqual(57, self.water_system.count_water())

    def test_still_water_count_is_calculated(self):
        self.water_system.run_until_overflow()
        self.assertEqual(29, self.water_system.count_still_water())
