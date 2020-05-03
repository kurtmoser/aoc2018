from aoc2018.day08.license_node import LicenseNode
import unittest

class TestFoo(unittest.TestCase):
    def setUp(self):
        self.license_node = LicenseNode(list(map(int, '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split())))

    def test_cumulative_metadata_sum_gets_calculated(self):
        self.assertEqual(138, self.license_node.get_cumulative_metadata_sum())

    def test_complex_metadata_sum_gets_calculated(self):
        self.assertEqual(66, self.license_node.get_complex_metadata_sum())
