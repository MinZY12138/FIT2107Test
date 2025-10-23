"""Unit tests for user input functions with mocking."""

import unittest
from unittest.mock import patch
from src.user_input import (
    read_integer,
    read_float,
    read_integer_range,
    read_float_range,
)


class TestUserInput(unittest.TestCase):
    """Test cases for functions that read and validate user input."""

    @patch("builtins.input", side_effect=["10"])
    def test_read_integer_valid(self, _mock_input):
        """Should return integer when valid input is given."""
        result = read_integer("Enter: ")
        self.assertEqual(result, 10)

    @patch("builtins.input", side_effect=["abc", "5"])
    def test_read_integer_invalid_then_valid(self, _mock_input):
        """Should keep asking until a valid integer is given."""
        result = read_integer("Enter: ")
        self.assertEqual(result, 5)

    @patch("builtins.input", side_effect=["3.14"])
    def test_read_float_valid(self, _mock_input):
        """Should return float when valid input is given."""
        result = read_float("Enter: ")
        self.assertAlmostEqual(result, 3.14)

    @patch("builtins.input", side_effect=["abc", "2.71"])
    def test_read_float_invalid_then_valid(self, _mock_input):
        """Should re-prompt when invalid, then accept valid float."""
        result = read_float("Enter: ")
        self.assertAlmostEqual(result, 2.71)

    @patch("builtins.input", side_effect=["50"])
    def test_read_integer_range_valid(self, _mock_input):
        """Should return integer within range."""
        result = read_integer_range("Enter: ", 10, 100)
        self.assertEqual(result, 50)

    @patch("builtins.input", side_effect=["200", "30"])
    def test_read_integer_range_outside_then_valid(self, _mock_input):
        """Should re-prompt when outside range then accept valid."""
        result = read_integer_range("Enter: ", 10, 100)
        self.assertEqual(result, 30)

    @patch("builtins.input", side_effect=["1.2"])
    def test_read_float_range_valid(self, _mock_input):
        """Should return float within range."""
        result = read_float_range("Enter: ", 0.5, 2.0)
        self.assertAlmostEqual(result, 1.2)

    @patch("builtins.input", side_effect=["5.5", "1.1"])
    def test_read_float_range_outside_then_valid(self, _mock_input):
        """Should re-prompt when outside range then accept valid."""
        result = read_float_range("Enter: ", 0.5, 2.0)
        self.assertAlmostEqual(result, 1.1)
