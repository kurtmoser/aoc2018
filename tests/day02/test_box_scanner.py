from aoc2018.day02.box_scanner import BoxScanner
import unittest

class TestBoxScanner(unittest.TestCase):
    def test_codes_containing_n_letters_of_one_type_are_recognized(self):
        scanner = BoxScanner()

        self.assertFalse(scanner.is_n_letter_code('abcdef', 2))
        self.assertTrue(scanner.is_n_letter_code('bababc', 2))
        self.assertTrue(scanner.is_n_letter_code('abbcde', 2))
        self.assertFalse(scanner.is_n_letter_code('abcccd', 2))

        self.assertFalse(scanner.is_n_letter_code('abcdef', 3))
        self.assertTrue(scanner.is_n_letter_code('bababc', 3))
        self.assertFalse(scanner.is_n_letter_code('abbcde', 3))
        self.assertTrue(scanner.is_n_letter_code('abcccd', 3))

    def test_codes_differing_by_one_are_recognized(self):
        scanner = BoxScanner()

        self.assertFalse(scanner.codes_differ_by_one('abcde', 'axcye'))
        self.assertTrue(scanner.codes_differ_by_one('fghij', 'fguij'))

if __name__ == '__main__':
    unittest.main()
