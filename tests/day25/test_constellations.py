from aoc2018.day25.constellations import Constellations
import unittest

class TestConstellations(unittest.TestCase):
    def test_constellation_are_merged(self):
        system = Constellations([
            [0,0,0,0],
            [3,0,0,0],
            [0,3,0,0],
            [0,0,3,0],
            [0,0,0,3],
            [0,0,0,6],
            [9,0,0,0],
            [12,0,0,0],
        ])
        system.build_constellations()
        self.assertEqual(2, len(system.constellations))
