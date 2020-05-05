from aoc2018.day12.greenhouse import Greenhouse
import unittest

class TestGreenhouse(unittest.TestCase):
    def setUp(self):
        self.greenhouse = Greenhouse()
        self.greenhouse.set_rules({
            '...##': '#',
            '..#..': '#',
            '.#...': '#',
            '.#.#.': '#',
            '.#.##': '#',
            '.##..': '#',
            '.####': '#',
            '#.#.#': '#',
            '#.###': '#',
            '##.#.': '#',
            '##.##': '#',
            '###..': '#',
            '###.#': '#',
            '####.': '#',
        })

    def test_plants_evolve(self):
        self.greenhouse.set_plants('#..#.#..##......###...###')
        self.greenhouse.evolve()
        self.assertEqual('#...#....#.....#..#..#..#', self.greenhouse.plants)
        self.greenhouse.evolve(19)
        self.assertEqual('#....##....#####...#######....#.#..##', self.greenhouse.plants)

    def test_plants_checksum_is_calculated(self):
        self.greenhouse.set_plants('#....##....#####...#######....#.#..##')
        self.greenhouse.start_pos = -2  # Need to tweak it to comply with data from example
        self.assertEqual(325, self.greenhouse.get_plants_checksum())
