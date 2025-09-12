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

LOAN_DAYS = {"Short": 7, "Medium": 14, "Long": 28}

def fees_str_to_float(outstanding_fees: str) -> float:
    return 10.0 if str(outstanding_fees).strip().lower() == "yes" else 0.0

def trained_str_to_bool(training: str) -> bool:
    return str(training).strip().lower() == "trained"

def age_bucket_to_int(patron_age: str) -> int:
    s = str(patron_age).strip()
    if s.startswith("<"):
        return 17
    if s.startswith(">=") or s.startswith("=>"):
        return 90
    if "-" in s:
        return 30
    try:
        return int(s)
    except Exception:
        return 30


class TestCanBorrow(unittest.TestCase):
    # 1 CarpentryTool, <18, Short, Fees=Yes, GardenTrained, CarpentryNotTrained -> NOT ALLOWED
    def test_deny_carpentry_u18_S_fee(self):
        result = can_borrow("CarpentryTool", age_bucket_to_int("<18"), LOAN_DAYS["Short"], fees_str_to_float("Yes"),
                            False,                                     # gardening N/A -> False
                            trained_str_to_bool("NotTrained"))         # carpentry from table
        self.assertEqual(result, False)

    # 2 GardeningTool, <18, Long, Fees=No, GardenNotTrained, CarpentryTrained -> NOT ALLOWED
    def test_deny_gardening_u18_L_nofee(self):
        result = can_borrow("GardeningTool", age_bucket_to_int("<18"), LOAN_DAYS["Long"], fees_str_to_float("No"),
                            trained_str_to_bool("NotTrained"),         # gardening from table
                            False)                                     # carpentry N/A -> False
        self.assertEqual(result, False)

    # 3 Book, 90+, Medium, Fees=Yes -> ALLOW
    def test_allow_book_90p_M_fee(self):
        result = can_borrow("Book", age_bucket_to_int(">=90"), LOAN_DAYS["Medium"], fees_str_to_float("Yes"),
                            False, False)                               # both N/A
        self.assertEqual(result, True)

    # 4 Book, adult, Medium, Fees=No -> ALLOW
    def test_allow_book_adult_M_nofee(self):
        result = can_borrow("Book", age_bucket_to_int("18-89"), LOAN_DAYS["Medium"], fees_str_to_float("No"),
                            False, False)
        self.assertEqual(result, True)

    # 5 Book, 90+, Long, Fees=No -> ALLOW
    def test_allow_book_90p_L_nofee(self):
        result = can_borrow("Book", age_bucket_to_int(">=90"), LOAN_DAYS["Long"], fees_str_to_float("No"),
                            False, False)
        self.assertEqual(result, True)

    # 6 CarpentryTool, adult, Short, Fees=Yes, CarpentryTrained -> NOT ALLOWED
    def test_deny_carpentry_adult_S_fee(self):
        result = can_borrow("CarpentryTool", age_bucket_to_int("18-89"), LOAN_DAYS["Short"], fees_str_to_float("Yes"),
                            False,
                            trained_str_to_bool("Trained"))
        self.assertEqual(result, False)

    # 7 CarpentryTool, 90+, Long, Fees=No, CarpentryTrained -> NOT ALLOWED
    def test_deny_carpentry_90p_L_nofee(self):
        result = can_borrow("CarpentryTool", age_bucket_to_int(">=90"), LOAN_DAYS["Long"], fees_str_to_float("No"),
                            False,
                            trained_str_to_bool("Trained"))
        self.assertEqual(result, False)

    # 8 Book, 90+, Short, Fees=No -> ALLOW
    def test_allow_book_90p_S_nofee(self):
        result = can_borrow("Book", age_bucket_to_int(">=90"), LOAN_DAYS["Short"], fees_str_to_float("No"),
                            False, False)
        self.assertEqual(result, True)

    # 9 CarpentryTool, <18, Medium, Fees=No, CarpentryTrained -> NOT ALLOWED
    def test_deny_carpentry_u18_M_nofee(self):
        result = can_borrow("CarpentryTool", age_bucket_to_int("<18"), LOAN_DAYS["Medium"], fees_str_to_float("No"),
                            False,
                            trained_str_to_bool("Trained"))
        self.assertEqual(result, False)

    # 10 GardeningTool, 90+, Medium, Fees=Yes, GardenTrained -> NOT ALLOWED
    def test_deny_gardening_90p_M_fee(self):
        result = can_borrow("GardeningTool", age_bucket_to_int(">=90"), LOAN_DAYS["Medium"], fees_str_to_float("Yes"),
                            trained_str_to_bool("Trained"),
                            False)
        self.assertEqual(result, False)

    # 11 GardeningTool, adult, Long, Fees=Yes, GardenTrained -> NOT ALLOWED
    def test_deny_gardening_adult_L_fee(self):
        result = can_borrow("GardeningTool", age_bucket_to_int("18-89"), LOAN_DAYS["Long"], fees_str_to_float("Yes"),
                            trained_str_to_bool("Trained"),
                            False)
        self.assertEqual(result, False)

    # 12 GardeningTool, <18, Short, Fees=Yes, GardenNotTrained -> NOT ALLOWED
    def test_deny_gardening_u18_S_fee(self):
        result = can_borrow("GardeningTool", age_bucket_to_int("<18"), LOAN_DAYS["Short"], fees_str_to_float("Yes"),
                            trained_str_to_bool("NotTrained"),
                            False)
        self.assertEqual(result, False)

    # 13 Book, <18, Medium, Fees=No -> ALLOW
    def test_allow_book_u18_M_nofee(self):
        result = can_borrow("Book", age_bucket_to_int("<18"), LOAN_DAYS["Medium"], fees_str_to_float("No"),
                            False, False)
        self.assertEqual(result, True)


