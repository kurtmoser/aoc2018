from aoc2018.day05.polymer import Polymer
import unittest

class TestPolymer(unittest.TestCase):
    def test_polymer_gets_reduced(self):
        polymer = Polymer('dabAcCaCBAcCcaDA')
        self.assertEqual('dabCBAcaDA', polymer.reduce())
