from aoc2018.day15.beverage_battle import BeverageBattle
import unittest

class TestBeverageBattle(unittest.TestCase):
    def test_battle_is_fought_out(self):
        battle = BeverageBattle([
            '#######',
            '#.G...#',
            '#...EG#',
            '#.#.#G#',
            '#..G#E#',
            '#.....#',
            '#######',
        ])
        battle.simulate()
        self.assertEqual(27730, battle.round * sum(unit['health'] for unit in battle.units))
