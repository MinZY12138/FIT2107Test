# tests/test_user_input.py
import unittest
import sys
from io import StringIO
from contextlib import contextmanager, redirect_stdout

from src.user_input import (
    is_int,
    is_float,
    read_string,
    read_integer,
    read_float,
    read_integer_range,
    read_float_range,
    read_bool,
)

# ---- helper: simulate stdin without定义任何类（保持每文件仅1个class）----
@contextmanager
def simulate_input(text: str):
    old = sys.stdin
    try:
        sys.stdin = StringIO(text)
        yield
    finally:
        sys.stdin = old


class TestUserInput(unittest.TestCase):
    """Unit tests for user_input helpers; one assert per test."""

    # ------- is_int -------
    def test_is_int_true_for_digits(self):
        self.assertTrue(is_int("10"))

    def test_is_int_false_for_nondigits(self):
        self.assertFalse(is_int("abc"))

    # ------- is_float -------
    def test_is_float_true_for_decimal(self):
        self.assertTrue(is_float("3.14"))

    def test_is_float_false_for_bad_format(self):
        self.assertFalse(is_float("a.5"))

    # ------- read_string -------
    def test_read_string_returns_line_without_newline(self):
        with simulate_input("hello\n"):
            self.assertEqual(read_string("Enter: "), "hello")

    # ------- read_integer -------
    def test_read_integer_returns_value_after_retry(self):
        with simulate_input("abc\n5\n"), redirect_stdout(StringIO()):
            self.assertEqual(read_integer("Enter: "), 5)

    def test_read_integer_prints_error_on_invalid(self):
        out = StringIO()
        with simulate_input("abc\n5\n"), redirect_stdout(out):
            read_integer("Enter: ")
        self.assertIn("Please enter a whole number.", out.getvalue())

    # ------- read_float -------
    def test_read_float_returns_value_after_retry(self):
        with simulate_input("x\n2.5\n"), redirect_stdout(StringIO()):
            self.assertAlmostEqual(read_float("Enter: "), 2.5)

    def test_read_float_prints_error_on_invalid(self):
        out = StringIO()
        with simulate_input("x\n2.5\n"), redirect_stdout(out):
            read_float("Enter: ")
        self.assertIn("Please enter a decimal number.", out.getvalue())

    # ------- read_integer_range -------
    def test_read_integer_range_returns_in_range_after_retry(self):
        with simulate_input("100\n3\n"), redirect_stdout(StringIO()):
            self.assertEqual(read_integer_range("Enter: ", 1, 5), 3)

    def test_read_integer_range_prints_range_hint(self):
        out = StringIO()
        with simulate_input("100\n3\n"), redirect_stdout(out):
            read_integer_range("Enter: ", 1, 5)
        self.assertIn("Please enter a value between 1 and 5", out.getvalue())

    # ------- read_float_range -------
    def test_read_float_range_returns_in_range_after_retry(self):
        with simulate_input("9.9\n2.5\n"), redirect_stdout(StringIO()):
            self.assertAlmostEqual(read_float_range("Enter: ", 1.0, 5.0), 2.5)

    def test_read_float_range_prints_range_hint(self):
        out = StringIO()
        with simulate_input("9.9\n2.5\n"), redirect_stdout(out):
            read_float_range("Enter: ", 1.0, 5.0)
        self.assertIn("Please enter a value between 1.0 and 5.0", out.getvalue())

    # ------- read_bool -------
    def test_read_bool_returns_y_after_retry(self):
        with simulate_input("x\nY\n"), redirect_stdout(StringIO()):
            self.assertEqual(read_bool("Enter y/n: "), "y")

    def test_read_bool_prints_error_on_invalid(self):
        out = StringIO()
        with simulate_input("x\nY\n"), redirect_stdout(out):
            read_bool("Enter y/n: ")
        self.assertIn("Please enter 'y' or 'n'", out.getvalue())
