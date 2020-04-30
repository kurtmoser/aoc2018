from aoc2018.day03.canvas import Canvas
import unittest

class TestFoo(unittest.TestCase):
    def test_canvas_overlaps_are_calculated(self):
        canvas = Canvas()
        canvas.add_slices([
            '#1 @ 1,3: 4x4',
            '#2 @ 3,1: 4x4',
            '#3 @ 5,5: 2x2',
        ])
        self.assertEqual(4, canvas.get_overlaps_count())

    def test_canvas_nonoverlap_is_found(self):
        canvas = Canvas()
        canvas.add_slices([
            '#1 @ 1,3: 4x4',
            '#2 @ 3,1: 4x4',
            '#3 @ 5,5: 2x2',
        ])
        self.assertEqual(3, canvas.get_nonoverlapping_claim_id())
