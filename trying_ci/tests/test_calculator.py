"""Unit tests for the Calculator class."""

import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Tests for the Calculator class."""

    def setUp(self):
        """Set up a Calculator instance for each test."""
        pass

    def test_initial_answer(self):
        """Test that a new Calculator starts with an answer of zero."""
        calc = Calculator()
        self.assertEqual(0, calc.get_answer())
