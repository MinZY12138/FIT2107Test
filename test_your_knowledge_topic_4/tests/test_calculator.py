# Student name: Min Zhengyuan
# Student ID: 34075887

import unittest

from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_initial_answer(self):
        self.assertEqual(0, self.calc.get_answer())

    def test_add(self):
        self.calc.add(5)
        self.assertEqual(5, self.calc.get_answer())

    def test_subtract(self):
        self.calc.subtract(3)
        self.assertEqual(-3, self.calc.get_answer())

    def test_multiply(self):
        self.calc.add(2).multiply(4)   # (0+2)*4 = 8
        self.assertEqual(8, self.calc.get_answer())

    def test_power(self):
        self.calc.add(2).power(3)      # (0+2)^3 = 8
        self.assertEqual(8, self.calc.get_answer())

    def test_reset(self):
        self.calc.add(10).reset()
        self.assertEqual(0, self.calc.get_answer())

if __name__ == "__main__":
    unittest.main()