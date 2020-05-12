from aoc2018.day24.pandemic import Pandemic
import unittest

class TestPandemic(unittest.TestCase):
    def setUp(self):
        self.pandemic_data = [
            'Immune System:',
            '17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2',
            '989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3',
            '',
            'Infection:',
            '801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1',
            '4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4',
        ]

    def test_battle_is_simulated(self):
        pandemic = Pandemic(self.pandemic_data)
        pandemic.simulate()
        self.assertEqual(5216, sum(group['units'] for group in pandemic.groups))

    def test_immune_system_boost_is_supported(self):
        pandemic = Pandemic(self.pandemic_data, 1570)
        pandemic.simulate()
        self.assertEqual(51, sum(group['units'] for group in pandemic.groups))
