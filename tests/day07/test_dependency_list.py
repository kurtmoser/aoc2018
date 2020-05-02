from aoc2018.day07.dependency_list import DependencyList
import unittest

class TestDependencyList(unittest.TestCase):
    def setUp(self):
        self.deps_list = DependencyList([
            ('C', 'A'),
            ('C', 'F'),
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'E'),
            ('D', 'E'),
            ('F', 'E'),
        ])

    def test_construction_order_gets_resolved(self):
        self.assertEqual('CABDFE', self.deps_list.get_resolve_order())

    def test_construction_time_gets_calculated(self):
        self.assertEqual(15, self.deps_list.get_construction_time(2, step_time_add=0))
