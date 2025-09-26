'''
The method you are testing is: 
    can_borrow(item_type, patron_age, length_of_loan, outstanding_fees, gardening_training, carpentry_training)

The data type of each parameter is:
- item_type: string
- patron_age: integer
- length_of_loan: integer
- outstanding_fees: float
- gardening_training: boolean
- carpentry_training: boolean

You can assume that the can_borrow method is already imported into this python module,
so you can call "can_borrow" directly.

Author: Min Zhengyuan
Student ID: 34075887
'''

import unittest
from src.borrow import can_borrow

# Simple constants are fine in tests
LOAN_DAYS = {"Short": 7, "Medium": 14, "Long": 28}

class TestCanBorrow(unittest.TestCase):
    # 1 CarpentryTool, <18, Short, Fees=Yes, CarpentryNotTrained -> DENY
    def test_deny_carpentry_under18_short_with_fees_carpentry_not_trained(self):
        result = can_borrow("CarpentryTool", 17, LOAN_DAYS["Short"], 10.0,
                            gardening_training=False, carpentry_training=False)
        self.assertFalse(result, "Failed: CarpentryTool under 18 with fees and not trained should be denied")

    # 2 GardeningTool, <18, Long, Fees=No, GardeningNotTrained -> DENY
    def test_deny_gardening_under18_long_no_fees_gardening_not_trained(self):
        result = can_borrow("GardeningTool", 17, LOAN_DAYS["Long"], 0.0,
                            gardening_training=False, carpentry_training=False)
        self.assertFalse(result, "Failed: GardeningTool under 18 with no fees and not trained should be denied")

    # 3 Book, 90+, Medium, Fees=Yes -> ALLOW
    def test_allow_book_age90plus_medium_with_fees(self):
        result = can_borrow("Book", 90, LOAN_DAYS["Medium"], 10.0,
                            gardening_training=False, carpentry_training=False)
        self.assertTrue(result, "Failed: Book age 90+ with fees should be allowed")

    # 4 Book, adult(30), Medium, Fees=No -> ALLOW
    def test_allow_book_adult_medium_no_fees(self):
        result = can_borrow("Book", 30, LOAN_DAYS["Medium"], 0.0,
                            gardening_training=False, carpentry_training=False)
        self.assertTrue(result, "Failed: Book adult with no fees should be allowed")

    # 5 Book, 90+, Long, Fees=No -> ALLOW
    def test_allow_book_age90plus_long_no_fees(self):
        result = can_borrow("Book", 90, LOAN_DAYS["Long"], 0.0,
                            gardening_training=False, carpentry_training=False)
        self.assertTrue(result, "Failed: Book age 90+ long loan with no fees should be allowed")

    # 6 CarpentryTool, adult(30), Short, Fees=Yes, CarpentryTrained -> DENY
    def test_deny_carpentry_adult_short_with_fees_carpentry_trained(self):
        result = can_borrow("CarpentryTool", 30, LOAN_DAYS["Short"], 10.0,
                            gardening_training=False, carpentry_training=True)
        self.assertFalse(result, "Failed: CarpentryTool adult short loan with fees even if trained should be denied")

    # 7 CarpentryTool, 90+, Long, Fees=No, CarpentryTrained -> DENY
    def test_deny_carpentry_age90plus_long_no_fees_carpentry_trained(self):
        result = can_borrow("CarpentryTool", 90, LOAN_DAYS["Long"], 0.0,
                            gardening_training=False, carpentry_training=True)
        self.assertFalse(result, "Failed: CarpentryTool age 90+ long loan with no fees should be denied")

    # 8 Book, 90+, Short, Fees=No -> ALLOW
    def test_allow_book_age90plus_short_no_fees(self):
        result = can_borrow("Book", 90, LOAN_DAYS["Short"], 0.0,
                            gardening_training=False, carpentry_training=False)
        self.assertTrue(result, "Failed: Book age 90+ short loan with no fees should be allowed")

    # 9 CarpentryTool, <18, Medium, Fees=No, CarpentryTrained -> DENY
    def test_deny_carpentry_under18_medium_no_fees_carpentry_trained(self):
        result = can_borrow("CarpentryTool", 17, LOAN_DAYS["Medium"], 0.0,
                            gardening_training=False, carpentry_training=True)
        self.assertFalse(result, "Failed: CarpentryTool under 18 medium loan with no fees should be denied")

    # 10 GardeningTool, 90+, Medium, Fees=Yes, GardeningTrained -> DENY
    def test_deny_gardening_age90plus_medium_with_fees_gardening_trained(self):
        result = can_borrow("GardeningTool", 90, LOAN_DAYS["Medium"], 10.0,
                            gardening_training=True, carpentry_training=False)
        self.assertFalse(result, "Failed: GardeningTool age 90+ medium loan with fees should be denied")

    # 11 GardeningTool, adult(30), Long, Fees=Yes, GardeningTrained -> DENY
    def test_deny_gardening_adult_long_with_fees_gardening_trained(self):
        result = can_borrow("GardeningTool", 30, LOAN_DAYS["Long"], 10.0,
                            gardening_training=True, carpentry_training=False)
        self.assertFalse(result, "Failed: GardeningTool adult long loan with fees should be denied")

    # 12 GardeningTool, <18, Short, Fees=Yes, GardeningNotTrained -> DENY
    def test_deny_gardening_under18_short_with_fees_gardening_not_trained(self):
        result = can_borrow("GardeningTool", 17, LOAN_DAYS["Short"], 10.0,
                            gardening_training=False, carpentry_training=False)
        self.assertFalse(result, "Failed: GardeningTool under 18 short loan with fees and not trained should be denied")

    # 13 Book, <18, Medium, Fees=No -> ALLOW
    def test_allow_book_under18_medium_no_fees(self):
        result = can_borrow("Book", 17, LOAN_DAYS["Medium"], 0.0,
                            gardening_training=False, carpentry_training=False)
        self.assertTrue(result, "Failed: Book under 18 medium loan with no fees should be allowed")



