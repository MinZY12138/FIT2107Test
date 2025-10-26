import unittest
from datetime import datetime

from src.loan import Loan


# Minimal item stub with the attributes used by Loan.__str__
class _Item:
    def __init__(self, item_id, name, type_):
        self._id = item_id
        self._name = name
        self._type = type_


class TestLoan(unittest.TestCase):
    def test_init_and_get_due_date(self):
        """Constructor should store item and due date; getter returns the same date."""
        item = _Item(7, "Hammer", "Tool")
        due = datetime(2024, 2, 29)  # leap-day to exercise date formatting edge
        loan = Loan(item, due)

        self.assertIs(loan._item, item)
        self.assertEqual(loan.get_due_date(), due)

    def test_str_format(self):
        """__str__ should include ID, name, type and a DD/MM/YYYY formatted date."""
        item = _Item(12, "Drill", "Carpentry")
        due = datetime(2025, 11, 5)  # 05/11/2025
        loan = Loan(item, due)

        expected = "Item 12: Drill (Carpentry); due 05/11/2025"
        self.assertEqual(str(loan), expected)
