import unittest
import sys
from io import StringIO
from contextlib import redirect_stdout
from src.user_input import *

class TestUserInput(unittest.TestCase):

    # --- helper to simulate input ---
    def _simulate_input(self, input_text):
        """Temporarily replace sys.stdin with StringIO."""
        class _Ctx:
            def __init__(self, outer, txt):
                self.outer = outer
                self.txt = txt
            def __enter__(self):
                self.old_stdin = sys.stdin
                sys.stdin = StringIO(self.txt)
            def __exit__(self, exc_type, exc_val, exc_tb):
                sys.stdin = self.old_stdin
        return _Ctx(self, input_text)

    # --- is_int / is_float ---
    def test_is_int(self):
        self.assertTrue(is_int("10"))
        self.assertFalse(is_int("abc"))

    def test_is_float(self):
        self.assertTrue(is_float("3.14"))
        self.assertFalse(is_float("a.5"))

    # --- read_string ---
    def test_read_string(self):
        with self._simulate_input("hello\n"):
            s = read_string("Enter: ")
            self.assertEqual(s, "hello")

    # --- read_integer: invalid then valid ---
    def test_read_integer_invalid_then_valid(self):
        out = StringIO()
        with self._simulate_input("abc\n5\n"), redirect_stdout(out):
            n = read_integer("Enter: ")
        self.assertEqual(n, 5)
        self.assertIn("Please enter a whole number.", out.getvalue())

    # --- read_float: invalid then valid ---
    def test_read_float_invalid_then_valid(self):
        out = StringIO()
        with self._simulate_input("x\n2.5\n"), redirect_stdout(out):
            n = read_float("Enter: ")
        self.assertAlmostEqual(n, 2.5)
        self.assertIn("Please enter a decimal number.", out.getvalue())

    # --- read_integer_range: out of range then valid ---
    def test_read_integer_range_out_then_ok(self):
        out = StringIO()
        with self._simulate_input("100\n3\n"), redirect_stdout(out):
            n = read_integer_range("Enter: ", 1, 5)
        self.assertEqual(n, 3)
        self.assertIn("Please enter a value between 1 and 5", out.getvalue())

    # --- read_float_range: out of range then valid ---
    def test_read_float_range_out_then_ok(self):
        out = StringIO()
        with self._simulate_input("9.9\n2.5\n"), redirect_stdout(out):
            n = read_float_range("Enter: ", 1.0, 5.0)
        self.assertAlmostEqual(n, 2.5)
        self.assertIn("Please enter a value between 1.0 and 5.0", out.getvalue())

    # --- read_bool: invalid then valid ---
    def test_read_bool_invalid_then_valid(self):
        out = StringIO()
        with self._simulate_input("x\nY\n"), redirect_stdout(out):
            b = read_bool("Enter y/n: ")
        self.assertEqual(b, "y")
        self.assertIn("Please enter 'y' or 'n'", out.getvalue())

if __name__ == "__main__":
    unittest.main()
