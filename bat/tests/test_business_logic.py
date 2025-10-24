import unittest
from src.business_logic import can_borrow
from  src.business_logic import can_borrow_book
from src.business_logic import type_of_patron
from src.business_logic import can_borrow_carpentry_tool
from src.business_logic import can_borrow_gardening_tool


class TestTypeOfPatron(unittest.TestCase):

    def test_negative_age(self):
        """Age < 0 → should return 'ERROR'"""
        self.assertEqual(type_of_patron(-1), "ERROR")

    def test_minor_lower_boundary(self):
        """Age = 0 → should return 'Minor'"""
        self.assertEqual(type_of_patron(0), "Minor")

    def test_minor_upper_boundary(self):
        """Age = 17 → still 'Minor'"""
        self.assertEqual(type_of_patron(17), "Minor")

    def test_adult_lower_boundary(self):
        """Age = 18 → should return 'Adult'"""
        self.assertEqual(type_of_patron(18), "Adult")

    def test_adult_typical(self):
        """Typical adult age (50)"""
        self.assertEqual(type_of_patron(50), "Adult")

    def test_elderly_boundary(self):
        """Age = 90 → should return 'Elderly'"""
        self.assertEqual(type_of_patron(90), "Elderly")


class TestCanBorrowBook(unittest.TestCase):
    def test_over_8_weeks(self):
        """Loan too long → should return False"""
        result = can_borrow_book(25, 60, 0)
        self.assertFalse(result)

    def test_has_fees(self):
        """Outstanding fees → should return False"""
        result = can_borrow_book(30, 20, 5)
        self.assertFalse(result)

    def test_no_fees_and_short_loan(self):
        """No fees, within 8 weeks → should return True"""
        result = can_borrow_book(40, 40, 0)
        self.assertTrue(result)

    def test_fees_reduced_but_not_zero(self):
        """Discount reduces but not clears fees → should return False"""
        result = can_borrow_book(20, 30, 10)  # assume small discount
        self.assertFalse(result)

    def test_discount_clears_fees(self):
        """If discount clears all fees → should return True"""
        result = can_borrow_book(70, 30, 0)  # old patrons get high discount
        self.assertTrue(result)


class TestCanBorrow(unittest.TestCase):
    def setUp(self):
        self.info = {
            "age": 30,
            "length": 7,
            "fees": 0.0,
            "gardening_training": True,
            "carpentry_training": True,
        }

    def test_dispatch_to_book(self):
        result = can_borrow("Book", self.info)
        expected = can_borrow_book(
            self.info["age"], self.info["length"], self.info["fees"]
        )
        self.assertEqual(result, expected)

    def test_dispatch_to_gardening_tool(self):
        result = can_borrow("Gardening tool", self.info)
        expected = can_borrow_gardening_tool(
            self.info["age"],
            self.info["length"],
            self.info["fees"],
            self.info["gardening_training"],
        )
        self.assertEqual(result, expected)

    def test_dispatch_to_carpentry_tool(self):
        result = can_borrow("Carpentry tool", self.info)
        expected = can_borrow_carpentry_tool(
            self.info["age"],
            self.info["length"],
            self.info["fees"],
            self.info["carpentry_training"],
        )
        self.assertEqual(result, expected)

    def test_unknown_type_returns_false(self):
        self.assertFalse(can_borrow("Unknown Item", self.info))


class TestCanBorrowGardeningTool(unittest.TestCase):

    def test_with_fees(self):
        """fees_owed > 0 → should return False"""
        result = can_borrow_gardening_tool(
            patron_age=30, 
            length_of_loan=10, 
            outstanding_fees=10.0, 
            gardening_tool_training=True
        )
        self.assertFalse(result)

    def test_over_loan_limit(self):
        """length_of_loan > 28 → should return False"""
        result = can_borrow_gardening_tool(
            patron_age=30, 
            length_of_loan=35, 
            outstanding_fees=0.0, 
            gardening_tool_training=True
        )
        self.assertFalse(result)

    def test_training_completed(self):
        """Valid case with training → should return True"""
        result = can_borrow_gardening_tool(
            patron_age=30, 
            length_of_loan=20, 
            outstanding_fees=0.0, 
            gardening_tool_training=True
        )
        self.assertTrue(result)

    def test_no_training(self):
        """Valid case without training → should return False"""
        result = can_borrow_gardening_tool(
            patron_age=30, 
            length_of_loan=20, 
            outstanding_fees=0.0, 
            gardening_tool_training=False
        )
        self.assertFalse(result)

    def test_senior_discount_reduces_fees(self):
        """Older patron gets discount that clears all fees → should return True"""
        result = can_borrow_gardening_tool(
            patron_age=90, 
            length_of_loan=20, 
            outstanding_fees=10.0, 
            gardening_tool_training=True
        )
        self.assertTrue(result)