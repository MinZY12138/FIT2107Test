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


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_positive(self):
        self.calc.add(5)
        self.assertEqual(self.calc.get_answer(), 5)

    def test_add_negative(self):
        self.calc.add(-3)
        self.assertEqual(self.calc.get_answer(), -3)


class TestSubtract(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_subtract_positive(self):
        self.calc.subtract(3)
        self.assertEqual(self.calc.get_answer(), -3)

    def test_subtract_negative(self):
        self.calc.subtract(-4)
        self.assertEqual(self.calc.get_answer(), 4)


class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_multiply_simple(self):
        # set initial state directly to avoid depending on add()
        self.calc._answer = 3
        self.calc.multiply(4)
        self.assertEqual(self.calc.get_answer(), 12)

    def test_multiply_by_zero(self):
        # starting from 0: 0 * n = 0
        self.calc.multiply(5)
        self.assertEqual(self.calc.get_answer(), 0)

    def test_multiply_by_negative(self):
        self.calc._answer = -2
        self.calc.multiply(3)
        self.assertEqual(self.calc.get_answer(), -6)


class TestPower(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_power_basic(self):
        self.calc._answer = 2
        self.calc.power(3)  # 2 ** 3 = 8
        self.assertEqual(self.calc.get_answer(), 8)

    def test_power_zero(self):
        self.calc._answer = 5
        self.calc.power(0)  # 5 ** 0 = 1
        self.assertEqual(self.calc.get_answer(), 1)

    def test_power_one(self):
        self.calc._answer = 7
        self.calc.power(1)  # 7 ** 1 = 7
        self.assertEqual(self.calc.get_answer(), 7)


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