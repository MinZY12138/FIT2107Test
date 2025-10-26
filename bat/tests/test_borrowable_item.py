import unittest
from src.borrowable_item import BorrowableItem


class TestBorrowableItem(unittest.TestCase):
    def test_init_defaults(self):
        """__init__ should set all fields to 'NO DATA LOADED'."""
        b = BorrowableItem()
        self.assertEqual(b._id, "NO DATA LOADED")
        self.assertEqual(b._name, "NO DATA LOADED")
        self.assertEqual(b._type, "NO DATA LOADED")
        self.assertEqual(b._year, "NO DATA LOADED")
        self.assertEqual(b._number_owned, "NO DATA LOADED")
        self.assertEqual(b._on_loan, "NO DATA LOADED")

        # __str__ before loading should reflect defaults
        expected = (
            "Item NO DATA LOADED: NO DATA LOADED (NO DATA LOADED)\n"
            "Year: NO DATA LOADED\n"
            "NO DATA LOADED/NO DATA LOADED on loan"
        )
        self.assertEqual(str(b), expected)

    def test_load_data_sets_fields_and_types(self):
        """load_data should assign fields and cast numeric strings to int."""
        record = {
            "item_id": "10",          # strings on purpose to test int() casts
            "item_name": "Hammer",
            "item_type": "Tool",
            "year": "2024",
            "number_owned": "3",
            "on_loan": "1",
        }
        b = BorrowableItem()
        b.load_data(record)

        self.assertEqual((b._id, b._name, b._type), (10, "Hammer", "Tool"))
        self.assertEqual((b._year, b._number_owned, b._on_loan), (2024, 3, 1))
        # ensure types are ints
        self.assertIsInstance(b._id, int)
        self.assertIsInstance(b._year, int)
        self.assertIsInstance(b._number_owned, int)
        self.assertIsInstance(b._on_loan, int)

    def test_str_after_load(self):
        """__str__ after load_data should format all three lines correctly."""
        b = BorrowableItem()
        b.load_data({
            "item_id": 12,
            "item_name": "Drill",
            "item_type": "Carpentry tool",
            "year": 2025,
            "number_owned": 5,
            "on_loan": 2,
        })
        expected = (
            "Item 12: Drill (Carpentry tool)\n"
            "Year: 2025\n"
            "2/5 on loan"
        )
        self.assertEqual(str(b), expected)
