import unittest
from unittest.mock import patch
from src.user_input import read_integer, read_float, read_integer_range, read_float_range

class TestUserInput(unittest.TestCase):

    @patch("builtins.input", side_effect=["10"])
    def test_read_integer_valid(self, mock_input):
        result = read_integer("Enter: ")
        self.assertEqual(result, 10)

    @patch("builtins.input", side_effect=["abc", "5"])
    def test_read_integer_invalid_then_valid(self, mock_input):
        result = read_integer("Enter: ")
        self.assertEqual(result, 5)

    @patch("builtins.input", side_effect=["3.14"])
    def test_read_float_valid(self, mock_input):
        result = read_float("Enter: ")
        self.assertAlmostEqual(result, 3.14)

    @patch("builtins.input", side_effect=["abc", "2.71"])
    def test_read_float_invalid_then_valid(self, mock_input):
        result = read_float("Enter: ")
        self.assertAlmostEqual(result, 2.71)

    @patch("builtins.input", side_effect=["50"])
    def test_read_integer_range_valid(self, mock_input):
        result = read_integer_range("Enter: ", 10, 100)
        self.assertEqual(result, 50)

    @patch("builtins.input", side_effect=["200", "30"])
    def test_read_integer_range_outside_then_valid(self, mock_input):
        result = read_integer_range("Enter: ", 10, 100)
        self.assertEqual(result, 30)

    @patch("builtins.input", side_effect=["1.2"])
    def test_read_float_range_valid(self, mock_input):
        result = read_float_range("Enter: ", 0.5, 2.0)
        self.assertAlmostEqual(result, 1.2)

    @patch("builtins.input", side_effect=["5.5", "1.1"])
    def test_read_float_range_outside_then_valid(self, mock_input):
        result = read_float_range("Enter: ", 0.5, 2.0)
        self.assertAlmostEqual(result, 1.1)
