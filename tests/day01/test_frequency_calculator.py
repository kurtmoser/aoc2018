from aoc2018.day01.frequency_calculator import FrequencyCalculator
import unittest

class TestFrequencyCalculator(unittest.TestCase):
    def test_resulting_frequency_gets_calculated(self):
        calc = FrequencyCalculator()

        calc.load_data(['+1', '+1', '+1'])
        self.assertEqual(3, calc.get_resulting_frequency())

        calc.load_data(['+1', '+1', '-2'])
        self.assertEqual(0, calc.get_resulting_frequency())

        calc.load_data(['-1', '-2', '-3'])
        self.assertEqual(-6, calc.get_resulting_frequency())

    def test_repeating_frequency_gets_calculated(self):
        calc = FrequencyCalculator()

        calc.load_data(['+1', '-1'])
        self.assertEqual(0, calc.get_repeating_frequency())

        calc.load_data(['+3', '+3', '+4', '-2', '-4'])
        self.assertEqual(10, calc.get_repeating_frequency())

        calc.load_data(['-6', '+3', '+8', '+5', '-6'])
        self.assertEqual(5, calc.get_repeating_frequency())

        calc.load_data(['+7', '+7', '-2', '-7', '-4'])
        self.assertEqual(14, calc.get_repeating_frequency())

if __name__ == '__main__':
    unittest.main()
