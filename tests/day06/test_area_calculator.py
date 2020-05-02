from aoc2018.day06.area_calculator import AreaCalculator
import unittest

class TestFoo(unittest.TestCase):
    def setUp(self):
        self.calc = AreaCalculator([
            (1, 1),
            (1, 6),
            (8, 3),
            (3, 4),
            (5, 5),
            (8, 9),
        ]);

    def test_detects_infinite_areas(self):
        self.assertEqual({0, 1, 2, 5}, self.calc.get_infinite_areas())

    def test_calculates_largest_noninfinite_area(self):
        self.assertEqual(17, self.calc.get_largest_noninfinite_area())

    def test_calculates_central_area(self):
        self.assertEqual(16, self.calc.get_central_area(32))
