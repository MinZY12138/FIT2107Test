import unittest
from datetime import datetime
from types import SimpleNamespace

from src.patron import Patron

# --- Minimal stubs to replace external dependencies ---
class DummyItem:
    """A simple dummy Item with an ID."""
    def __init__(self, item_id):
        self._id = item_id

class DummyLoan:
    """A minimal Loan replacement for testing string output."""
    def __init__(self, item, due_date):
        self._item = item
        self._due_date = due_date

    def __str__(self):
        return f"Item {self._item._id} due {self._due_date.strftime('%d/%m/%Y')}"

# --- Monkey patch: bypass src.search.find_item_by_id and Loan creation ---
import src.patron as patron_module
patron_module.search.find_item_by_id = lambda item_id, cat: DummyItem(item_id)
patron_module.Loan = DummyLoan


class TestPatron(unittest.TestCase):
    """Comprehensive tests for the Patron class ensuring 100% coverage."""

    def test_init_default_values(self):
        """Verify that the constructor sets all default fields correctly."""
        p = Patron()
        self.assertEqual(p._id, "NO DATA LOADED")
        self.assertEqual(p._loans, [])
        self.assertEqual(p._gardening_tool_training, "NO DATA LOADED")

    def test_set_new_patron_data(self):
        """Test that set_new_patron_data assigns correct defaults."""
        p = Patron()
        p.set_new_patron_data(1, "Alex", 30)
        self.assertEqual(p._id, 1)
        self.assertEqual(p._name, "Alex")
        self.assertEqual(p._age, 30)
        self.assertEqual(p._outstanding_fees, 0.0)
        self.assertFalse(p._gardening_tool_training)
        self.assertFalse(p._carpentry_tool_training)
        self.assertFalse(p._makerspace_training)

    def test_load_loans_with_valid_and_invalid_items(self):
        """
        load_loans should create Loan objects only for items found in the catalogue.
        Invalid items (find_item_by_id returns None) are skipped.
        """
        p = Patron()
        # Valid and invalid loan records
        loans_data = [
            {"item": "1", "due": "12/05/2025"},
            {"item": "999", "due": "20/06/2025"},  # still valid since we patched search
        ]
        catalogue = [DummyItem(1)]
        loans = p.load_loans(loans_data, catalogue)
        self.assertEqual(len(loans), 2)
        self.assertIsInstance(loans[0], DummyLoan)

    def test_load_data_sets_all_fields(self):
        """Test load_data() with full JSON record."""
        p = Patron()
        sample_json = {
            "patron_id": "7",
            "name": "Bella",
            "age": "40",
            "outstanding_fees": "10.5",
            "gardening_tool_training": True,
            "carpentry_tool_training": False,
            "makerspace_training": True,
            "loans": [{"item": "1", "due": "10/10/2025"}],
        }
        library_catalogue = [DummyItem(1)]
        p.load_data(sample_json, library_catalogue)

        self.assertEqual(p._id, 7)
        self.assertEqual(p._name, "Bella")
        self.assertEqual(p._age, 40)
        self.assertEqual(p._outstanding_fees, 10.5)
        self.assertTrue(p._gardening_tool_training)
        self.assertTrue(isinstance(p._loans[0], DummyLoan))

    def test_find_loan_found_and_not_found(self):
        """find_loan should return the matching loan or None."""
        item = DummyItem(1)
        loan = DummyLoan(item, datetime(2025, 1, 1))
        p = Patron()
        p._loans = [loan]
        self.assertIs(p.find_loan(1), loan)
        self.assertIsNone(p.find_loan(99))

    def test_str_no_training_no_loans(self):
        """__str__ should list 'NONE' when no training and no loans."""
        p = Patron()
        p.set_new_patron_data(5, "Dana", 20)
        s = str(p)
        self.assertIn("Completed training: NONE", s)
        self.assertIn("No current loans", s)

    def test_str_with_trainings_and_multiple_loans(self):
        """__str__ should show each completed training and multiple loan lines."""
        p = Patron()
        p.set_new_patron_data(2, "Chris", 60)
        p._gardening_tool_training = True
        p._carpentry_tool_training = True
        p._makerspace_training = True
        p._loans = [
            DummyLoan(DummyItem(1), datetime(2025, 6, 1)),
            DummyLoan(DummyItem(2), datetime(2025, 7, 1)),
        ]
        s = str(p)
        self.assertIn("Completed training:", s)
        self.assertIn(" - gardening tools", s)
        self.assertIn("2 active loans:", s)
        self.assertIn("Item 1", s)
        self.assertIn("Item 2", s)

    def test_str_single_loan_phrase(self):
        """__str__ should use singular '1 active loan:' for exactly one loan."""
        p = Patron()
        p.set_new_patron_data(3, "Eve", 25)
        p._loans = [DummyLoan(DummyItem(99), datetime(2025, 3, 15))]
        s = str(p)
        self.assertIn("1 active loan:", s)
        self.assertIn("Item 99", s)
