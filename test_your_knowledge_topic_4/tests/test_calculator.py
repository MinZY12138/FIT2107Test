# Student name: Min Zhengyuan
# Student ID: 34075887

import unittest

from src.calculator import Calculator


class TestInitialAndReset(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_initial_answer(self):
        self.assertEqual(self.calc.get_answer(), 0)

    def test_reset(self):
        # prepare some non-zero state, then reset
        self.calc._answer = 10
        self.calc.reset()
        self.assertEqual(self.calc.get_answer(), 0)

if __name__ == "__main__":
    unittest.main()