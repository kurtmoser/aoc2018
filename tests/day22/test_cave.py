from aoc2018.day22.cave import Cave
import unittest

class TestCave(unittest.TestCase):
    def test_risk_level_is_calculated(self):
        self.assertEqual(114, Cave(510, 10, 10).get_risk_level())

    def test_min_path_is_found(self):
        self.assertEqual(45, len(Cave(510, 10, 10).get_min_path()))
