from aoc2018.day18.magic_forest import MagicForest
import unittest

class TestMagicForest(unittest.TestCase):
    def test_forest_evolves(self):
        forest = MagicForest([
            '.#.#...|#.',
            '.....#|##|',
            '.|..|...#.',
            '..|#.....#',
            '#.#|||#|#|',
            '...#.||...',
            '.|....|...',
            '||...#|.#|',
            '|.||||..|.',
            '...#.|..|.',
        ])
        [forest.evolve() for _ in range(10)]
        self.assertEqual(1147, forest.get_resource_value())
