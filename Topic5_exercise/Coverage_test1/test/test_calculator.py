import unittest

from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        pass

    def test_initial_answer(self):
        calc = Calculator()
        self.assertEqual(0, calc.get_answer())

    def test_add(self):
        calc = Calculator()
        calc.add(10)
        self.assertEqual(10, calc.get_answer())

    def test_subtract(self):
        calc = Calculator()
        calc.add(10)
        calc.subtract(4)
        self.assertEqual(6, calc.get_answer())

    def test_multiply(self):
        calc = Calculator()
        calc.add(3)
        calc.multiply(5)
        self.assertEqual(15, calc.get_answer())

    def test_power(self):
        calc = Calculator()
        calc.add(2)
        calc.power(3)
        self.assertEqual(8, calc.get_answer())

    def test_reset(self):
        calc = Calculator()
        calc.add(100)
        calc.reset()
        self.assertEqual(0, calc.get_answer())