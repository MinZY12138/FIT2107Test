import unittest
from src.borrowable_item import BorrowableItem


class TestBorrowableItem(unittest.TestCase):


    # ---------- defaults after __init__ ----------

    def test_init_default_id(self):
        b = BorrowableItem()
        self.assertEqual(b._id, "NO DATA LOADED")

    def test_init_default_name(self):
        b = BorrowableItem()
        self.assertEqual(b._name, "NO DATA LOADED")

    def test_init_default_type(self):
        b = BorrowableItem()
        self.assertEqual(b._type, "NO DATA LOADED")

    def test_init_default_year(self):
        b = BorrowableItem()
        self.assertEqual(b._year, "NO DATA LOADED")

    def test_init_default_number_owned(self):
        b = BorrowableItem()
        self.assertEqual(b._number_owned, "NO DATA LOADED")

    def test_init_default_on_loan(self):
        b = BorrowableItem()
        self.assertEqual(b._on_loan, "NO DATA LOADED")

    def test_str_before_load_uses_defaults(self):
        b = BorrowableItem()
        expected = (
            "Item NO DATA LOADED: NO DATA LOADED (NO DATA LOADED)\n"
            "Year: NO DATA LOADED\n"
            "NO DATA LOADED/NO DATA LOADED on loan"
        )
        self.assertEqual(str(b), expected)

    # ---------- load_data casts/assigns ----------

    def test_load_data_sets_id_int(self):
        b = BorrowableItem()
        b.load_data({"item_id": "10", "item_name": "Hammer", "item_type": "Tool",
                     "year": "2024", "number_owned": "3", "on_loan": "1"})
        self.assertEqual(b._id, 10)

    def test_load_data_sets_name(self):
        b = BorrowableItem()
        b.load_data({"item_id": "10", "item_name": "Hammer", "item_type": "Tool",
                     "year": "2024", "number_owned": "3", "on_loan": "1"})
        self.assertEqual(b._name, "Hammer")

    def test_load_data_sets_type(self):
        b = BorrowableItem()
        b.load_data({"item_id": "10", "item_name": "Hammer", "item_type": "Tool",
                     "year": "2024", "number_owned": "3", "on_loan": "1"})
        self.assertEqual(b._type, "Tool")

    def test_load_data_sets_year_int(self):
        b = BorrowableItem()
        b.load_data({"item_id": "10", "item_name": "Hammer", "item_type": "Tool",
                     "year": "2024", "number_owned": "3", "on_loan": "1"})
        self.assertEqual(b._year, 2024)

    def test_load_data_sets_number_owned_int(self):
        b = BorrowableItem()
        b.load_data({"item_id": "10", "item_name": "Hammer", "item_type": "Tool",
                     "year": "2024", "number_owned": "3", "on_loan": "1"})
        self.assertEqual(b._number_owned, 3)

    def test_load_data_sets_on_loan_int(self):
        b = BorrowableItem()
        b.load_data({"item_id": "10", "item_name": "Hammer", "item_type": "Tool",
                     "year": "2024", "number_owned": "3", "on_loan": "1"})
        self.assertEqual(b._on_loan, 1)

    def test_id_is_instance_of_int_after_load(self):
        b = BorrowableItem()
        b.load_data({"item_id": "10", "item_name": "Hammer", "item_type": "Tool",
                     "year": "2024", "number_owned": "3", "on_loan": "1"})
        self.assertIsInstance(b._id, int)

    def test_year_is_instance_of_int_after_load(self):
        b = BorrowableItem()
        b.load_data({"item_id": "10", "item_name": "Hammer", "item_type": "Tool",
                     "year": "2024", "number_owned": "3", "on_loan": "1"})
        self.assertIsInstance(b._year, int)

    def test_number_owned_is_instance_of_int_after_load(self):
        b = BorrowableItem()
        b.load_data({"item_id": "10", "item_name": "Hammer", "item_type": "Tool",
                     "year": "2024", "number_owned": "3", "on_loan": "1"})
        self.assertIsInstance(b._number_owned, int)

    def test_on_loan_is_instance_of_int_after_load(self):
        b = BorrowableItem()
        b.load_data({"item_id": "10", "item_name": "Hammer", "item_type": "Tool",
                     "year": "2024", "number_owned": "3", "on_loan": "1"})
        self.assertIsInstance(b._on_loan, int)

    # ---------- __str__ formatting after load ----------

    def test_str_after_load_formats_three_lines(self):
        b = BorrowableItem()
        b.load_data({
            "item_id": 12,
            "item_name": "Drill",
            "item_type": "Carpentry tool",
            "year": 2025,
            "number_owned": 5,
            "on_loan": 2,
        })
        expected = "Item 12: Drill (Carpentry tool)\nYear: 2025\n2/5 on loan"
        self.assertEqual(str(b), expected)
