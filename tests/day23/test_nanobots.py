from aoc2018.day23.nanobots import Nanobots
import unittest

class TestNanobots(unittest.TestCase):
    def test_nanobots_in_range_is_counted(self):
        system = Nanobots([
            'pos=<0,0,0>, r=4',
            'pos=<1,0,0>, r=1',
            'pos=<4,0,0>, r=3',
            'pos=<0,2,0>, r=1',
            'pos=<0,5,0>, r=3',
            'pos=<0,0,3>, r=1',
            'pos=<1,1,1>, r=1',
            'pos=<1,1,2>, r=1',
            'pos=<1,3,1>, r=1',
        ])
        system.bots.sort(key=lambda i: i['range'], reverse=True)
        self.assertEqual(7, system.count_nanobots_in_range(system.bots[0]['pos'], system.bots[0]['range']))

    def test_closest_maximum_point_is_found(self):
        system = Nanobots([
            'pos=<10,12,12>, r=2',
            'pos=<12,14,12>, r=2',
            'pos=<16,12,12>, r=4',
            'pos=<14,14,14>, r=6',
            'pos=<50,50,50>, r=200',
            'pos=<10,10,10>, r=5',
        ])
        self.assertEqual(36, sum(system.get_maximum_point(100)))
