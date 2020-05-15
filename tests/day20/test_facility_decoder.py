from aoc2018.day20.facility_mapper import FacilityMapper
import unittest

class TestFacilityMapper(unittest.TestCase):
    def test_longest_path_is_found(self):
        mapper = FacilityMapper('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$')
        paths = mapper.get_long_paths()
        paths.sort(key=lambda i: len(i), reverse=True)
        self.assertEqual(31, len(paths[0]))
