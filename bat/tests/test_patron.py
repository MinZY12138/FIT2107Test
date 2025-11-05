import unittest
from datetime import datetime

from tests.dummy_item_for_patron import DummyItem
from tests.dummy_loan_for_patron import DummyLoan

# --- monkey patch Patron dependencies BEFORE import Patron class use ---
import src.patron as patron_module
patron_module.search.find_item_by_id = lambda item_id, cat: DummyItem(item_id)
patron_module.Loan = DummyLoan

from src.patron import Patron


class TestPatron(unittest.TestCase):
    """Unit tests for Patron; one assert per test where feasible."""

    # -------- init defaults --------
    def test_init_sets_default_id(self):
        self.assertEqual(Patron()._id, "NO DATA LOADED")

    def test_init_sets_default_loans_empty(self):
        self.assertEqual(Patron()._loans, [])

    def test_init_sets_default_training_flag(self):
        self.assertEqual(Patron()._gardening_tool_training, "NO DATA LOADED")

    # -------- set_new_patron_data --------
    def test_set_new_patron_data_sets_id(self):
        p = Patron(); p.set_new_patron_data(1, "Alex", 30)
        self.assertEqual(p._id, 1)

    def test_set_new_patron_data_sets_name(self):
        p = Patron(); p.set_new_patron_data(1, "Alex", 30)
        self.assertEqual(p._name, "Alex")

    def test_set_new_patron_data_sets_age(self):
        p = Patron(); p.set_new_patron_data(1, "Alex", 30)
        self.assertEqual(p._age, 30)

    def test_set_new_patron_data_sets_fees_zero(self):
        p = Patron(); p.set_new_patron_data(1, "Alex", 30)
        self.assertEqual(p._outstanding_fees, 0.0)

    def test_set_new_patron_data_sets_training_false(self):
        p = Patron(); p.set_new_patron_data(1, "Alex", 30)
        self.assertFalse(p._gardening_tool_training)

    def test_set_new_patron_data_sets_carpentry_false(self):
        p = Patron(); p.set_new_patron_data(1, "Alex", 30)
        self.assertFalse(p._carpentry_tool_training)

    def test_set_new_patron_data_sets_makerspace_false(self):
        p = Patron(); p.set_new_patron_data(1, "Alex", 30)
        self.assertFalse(p._makerspace_training)

    # -------- load_loans --------
    def test_load_loans_returns_two_entries(self):
        p = Patron()
        loans = p.load_loans(
            [{"item": "1", "due": "12/05/2025"}, {"item": "999", "due": "20/06/2025"}],
            [DummyItem(1)]
        )
        self.assertEqual(len(loans), 2)

    def test_load_loans_creates_dummyloan_instances(self):
        p = Patron()
        loans = p.load_loans(
            [{"item": "1", "due": "12/05/2025"}],
            [DummyItem(1)]
        )
        self.assertIsInstance(loans[0], DummyLoan)

    # -------- load_data --------
    def test_load_data_sets_id_int(self):
        p = Patron()
        p.load_data({
            "patron_id": "7", "name": "Bella", "age": "40",
            "outstanding_fees": "10.5",
            "gardening_tool_training": True,
            "carpentry_tool_training": False,
            "makerspace_training": True,
            "loans": [{"item": "1", "due": "10/10/2025"}],
        }, [DummyItem(1)])
        self.assertEqual(p._id, 7)

    def test_load_data_sets_name(self):
        p = Patron()
        p.load_data({
            "patron_id": "7", "name": "Bella", "age": "40",
            "outstanding_fees": "10.5",
            "gardening_tool_training": True,
            "carpentry_tool_training": False,
            "makerspace_training": True,
            "loans": [{"item": "1", "due": "10/10/2025"}],
        }, [DummyItem(1)])
        self.assertEqual(p._name, "Bella")

    def test_load_data_sets_age_int(self):
        p = Patron()
        p.load_data({
            "patron_id": "7", "name": "Bella", "age": "40",
            "outstanding_fees": "10.5",
            "gardening_tool_training": True,
            "carpentry_tool_training": False,
            "makerspace_training": True,
            "loans": [{"item": "1", "due": "10/10/2025"}],
        }, [DummyItem(1)])
        self.assertEqual(p._age, 40)

    def test_load_data_sets_fees_float(self):
        p = Patron()
        p.load_data({
            "patron_id": "7", "name": "Bella", "age": "40",
            "outstanding_fees": "10.5",
            "gardening_tool_training": True,
            "carpentry_tool_training": False,
            "makerspace_training": True,
            "loans": [{"item": "1", "due": "10/10/2025"}],
        }, [DummyItem(1)])
        self.assertEqual(p._outstanding_fees, 10.5)

    def test_load_data_sets_training_true(self):
        p = Patron()
        p.load_data({
            "patron_id": "7", "name": "Bella", "age": "40",
            "outstanding_fees": "10.5",
            "gardening_tool_training": True,
            "carpentry_tool_training": False,
            "makerspace_training": True,
            "loans": [{"item": "1", "due": "10/10/2025"}],
        }, [DummyItem(1)])
        self.assertTrue(p._gardening_tool_training)

    def test_load_data_creates_dummyloan(self):
        p = Patron()
        p.load_data({
            "patron_id": "7", "name": "Bella", "age": "40",
            "outstanding_fees": "10.5",
            "gardening_tool_training": True,
            "carpentry_tool_training": False,
            "makerspace_training": True,
            "loans": [{"item": "1", "due": "10/10/2025"}],
        }, [DummyItem(1)])
        self.assertIsInstance(p._loans[0], DummyLoan)

    # -------- find_loan --------
    def test_find_loan_returns_loan_when_found(self):
        item = DummyItem(1)
        p = Patron(); p._loans = [DummyLoan(item, datetime(2025, 1, 1))]
        self.assertIs(p.find_loan(1), p._loans[0])

    def test_find_loan_returns_none_when_not_found(self):
        p = Patron(); p._loans = []
        self.assertIsNone(p.find_loan(99))

    # -------- __str__ --------
    def test_str_none_training_and_no_loans(self):
        p = Patron(); p.set_new_patron_data(5, "Dana", 20)
        s = str(p)
        self.assertIn("Completed training: NONE", s)

    def test_str_none_loans_phrase(self):
        p = Patron(); p.set_new_patron_data(5, "Dana", 20)
        self.assertIn("No current loans", str(p))

    def test_str_three_trainings_listed(self):
        p = Patron(); p.set_new_patron_data(2, "Chris", 60)
        p._gardening_tool_training = True
        p._carpentry_tool_training = True
        p._makerspace_training = True
        p._loans = [DummyLoan(DummyItem(1), datetime(2025, 6, 1)),
                    DummyLoan(DummyItem(2), datetime(2025, 7, 1))]
        self.assertIn("Completed training:", str(p))

    def test_str_multiple_loans_header(self):
        p = Patron(); p.set_new_patron_data(2, "Chris", 60)
        p._loans = [DummyLoan(DummyItem(1), datetime(2025, 6, 1)),
                    DummyLoan(DummyItem(2), datetime(2025, 7, 1))]
        self.assertIn("2 active loans:", str(p))

    def test_str_single_loan_header(self):
        p = Patron(); p.set_new_patron_data(3, "Eve", 25)
        p._loans = [DummyLoan(DummyItem(99), datetime(2025, 3, 15))]
        self.assertIn("1 active loan:", str(p))
