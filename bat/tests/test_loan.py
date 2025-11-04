import unittest
from datetime import datetime

from .dummy_item_for_loan import ItemStub

from src.loan import Loan


class TestLoan(unittest.TestCase):
    """Unit tests for Loan with one-assert-per-test where feasible."""

    def test_init_stores_item_reference(self):
        item = ItemStub(7, "Hammer", "Tool")
        loan = Loan(item, datetime(2024, 2, 29))
        self.assertIs(loan._item, item)

    def test_get_due_date_returns_same_object(self):
        due = datetime(2024, 2, 29)  # leap day edge case
        loan = Loan(ItemStub(7, "Hammer", "Tool"), due)
        self.assertEqual(loan.get_due_date(), due)

    def test_str_formats_full_line(self):
        item = ItemStub(12, "Drill", "Carpentry")
        due = datetime(2025, 11, 5)  # -> 05/11/2025
        loan = Loan(item, due)
        expected = "Item 12: Drill (Carpentry); due 05/11/2025"
        self.assertEqual(str(loan), expected)
