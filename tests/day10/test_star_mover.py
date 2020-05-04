from aoc2018.day10.star_mover import StarMover
import unittest

class TestStarMover(unittest.TestCase):
    def setUp(self):
        self.star_mover = StarMover([
            [9, 1, 0, 2],
            [7, 0, -1, 0],
            [3, -2, -1, 1],
            [6, 10, -2, -1],
            [2, -4, 2, 2],
            [-6, 10, 2, -2],
            [1, 8, 1, -1],
            [1, 7, 1, 0],
            [-3, 11, 1, -2],
            [7, 6, -1, -1],
            [-2, 3, 1, 0],
            [-4, 3, 2, 0],
            [10, -3, -1, 1],
            [5, 11, 1, -2],
            [4, 7, 0, -1],
            [8, -2, 0, 1],
            [15, 0, -2, 0],
            [1, 6, 1, 0],
            [8, 9, 0, -1],
            [3, 3, -1, 1],
            [0, 5, 0, -1],
            [-2, 2, 2, 0],
            [5, -2, 1, 2],
            [1, 4, 2, 1],
            [-2, 7, 2, -2],
            [3, 6, -1, -1],
            [5, 0, 1, 0],
            [-6, 0, 2, 0],
            [5, 9, 1, -2],
            [14, 7, -2, 0],
            [-3, 6, 2, -1],
        ])

    def test_minimum_area_contains_answer(self):
        expected_string_representation = '\n'.join([
            'X   X  XXX',
            'X   X   X ',
            'X   X   X ',
            'XXXXX   X ',
            'X   X   X ',
            'X   X   X ',
            'X   X   X ',
            'X   X  XXX',
        ])
        self.star_mover.move_until_minimum_area()
        self.assertEqual(expected_string_representation, self.star_mover.to_string())

    def test_steps_to_minimum_area_gets_calculated(self):
        self.star_mover.move_until_minimum_area()
        self.assertEqual(3, self.star_mover.steps)
