from aoc2018.day14.chocolate_mixer import ChocolateMixer
import unittest

class TestChocolateMixer(unittest.TestCase):
    def test_recipes_after_position_are_calculated(self):
        self.assertEqual('5158916779', ChocolateMixer().get_recipes_after(9))
        self.assertEqual('0124515891', ChocolateMixer().get_recipes_after(5))
        self.assertEqual('9251071085', ChocolateMixer().get_recipes_after(18))
        self.assertEqual('5941429882', ChocolateMixer().get_recipes_after(2018))

    def test_recipes_before_pattern_are_counted(self):
        self.assertEqual(9, ChocolateMixer().count_recipes_before('51589'))
        self.assertEqual(5, ChocolateMixer().count_recipes_before('01245'))
        self.assertEqual(18, ChocolateMixer().count_recipes_before('92510'))
        self.assertEqual(2018, ChocolateMixer().count_recipes_before('59414'))
