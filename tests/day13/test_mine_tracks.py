from aoc2018.day13.mine_tracks import MineTracks
import unittest

class TestMineTracks(unittest.TestCase):
    def test_collision_is_detected(self):
        tracks = MineTracks([
            '/->-\        ',
            '|   |  /----\\',
            '| /-+--+-\  |',
            '| | |  | v  |',
            '\-+-/  \-+--/',
            '  \------/   ',
        ]);

        while not tracks.collisions:
            tracks.move_carts()

        self.assertEqual((7, 3), list(tracks.collisions.keys())[0])

    def test_collisions_are_cleaned_up(self):
        tracks = MineTracks([
            '/>-<\  ',
            '|   |  ',
            '| /<+-\\',
            '| | | v',
            '\>+</ |',
            '  |   ^',
            '  \<->/',
        ]);

        while len(tracks.carts) > 1:
            tracks.move_carts()
            tracks.remove_collisions()

        self.assertEqual((6, 4), (tracks.carts[0]['x'], tracks.carts[0]['y']))
