from aoc2018.day09.marble_game import MarbleGame
import unittest

class TestMarbleGame(unittest.TestCase):
    def test_it_calculates_top_score(self):
        self.assertEqual(32, MarbleGame(9, 25).get_winner_score())
        self.assertEqual(8317, MarbleGame(10, 1618).get_winner_score())
        self.assertEqual(146373, MarbleGame(13, 7999).get_winner_score())
        self.assertEqual(2764, MarbleGame(17, 1104).get_winner_score())
        self.assertEqual(54718, MarbleGame(21, 6111).get_winner_score())
        self.assertEqual(37305, MarbleGame(30, 5807).get_winner_score())
