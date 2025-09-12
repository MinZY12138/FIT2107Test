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

    def test_case_1(self):
        result = can_borrow("CarpentryTool", age_bucket_to_int("<18"), LOAN_DAYS["Short"],
                            fees_str_to_float("Yes"), trained_str_to_bool("Trained"), trained_str_to_bool("NotTrained"))
        self.assertEqual(result, False)

    def test_case_2(self):
        result = can_borrow("GardeningTool", age_bucket_to_int("<18"), LOAN_DAYS["Long"],
                            fees_str_to_float("No"), trained_str_to_bool("NotTrained"), trained_str_to_bool("Trained"))
        self.assertEqual(result, False)

    def test_case_3(self):
        result = can_borrow("Book", age_bucket_to_int(">=90"), LOAN_DAYS["Medium"],
                            fees_str_to_float("Yes"), trained_str_to_bool("Trained"), trained_str_to_bool("Trained"))
        self.assertEqual(result, True)

    def test_case_4(self):
        result = can_borrow("Book", age_bucket_to_int("18-89"), LOAN_DAYS["Medium"],
                            fees_str_to_float("No"), trained_str_to_bool("NotTrained"), trained_str_to_bool("NotTrained"))
        self.assertEqual(result, True)

    def test_case_5(self):
        result = can_borrow("Book", age_bucket_to_int(">=90"), LOAN_DAYS["Long"],
                            fees_str_to_float("No"), trained_str_to_bool("Trained"), trained_str_to_bool("NotTrained"))
        self.assertEqual(result, True)

    def test_case_6(self):
        result = can_borrow("CarpentryTool", age_bucket_to_int("18-89"), LOAN_DAYS["Short"],
                            fees_str_to_float("Yes"), trained_str_to_bool("NotTrained"), trained_str_to_bool("Trained"))
        self.assertEqual(result, False)

    def test_case_7(self):
        result = can_borrow("CarpentryTool", age_bucket_to_int(">=90"), LOAN_DAYS["Long"],
                            fees_str_to_float("No"), trained_str_to_bool("NotTrained"), trained_str_to_bool("Trained"))
        self.assertEqual(result, False)

    def test_case_8(self):
        result = can_borrow("Book", age_bucket_to_int(">=90"), LOAN_DAYS["Short"],
                            fees_str_to_float("No"), trained_str_to_bool("Trained"), trained_str_to_bool("Trained"))
        self.assertEqual(result, True)

    def test_case_9(self):
        result = can_borrow("CarpentryTool", age_bucket_to_int("<18"), LOAN_DAYS["Medium"],
                            fees_str_to_float("No"), trained_str_to_bool("Trained"), trained_str_to_bool("Trained"))
        self.assertEqual(result, False)

    def test_case_10(self):
        result = can_borrow("GardeningTool", age_bucket_to_int(">=90"), LOAN_DAYS["Medium"],
                            fees_str_to_float("Yes"), trained_str_to_bool("Trained"), trained_str_to_bool("NotTrained"))
        self.assertEqual(result, False)

    def test_case_11(self):
        result = can_borrow("GardeningTool", age_bucket_to_int("18-89"), LOAN_DAYS["Long"],
                            fees_str_to_float("Yes"), trained_str_to_bool("Trained"), trained_str_to_bool("NotTrained"))
        self.assertEqual(result, False)

    def test_case_12(self):
        result = can_borrow("GardeningTool", age_bucket_to_int("<18"), LOAN_DAYS["Short"],
                            fees_str_to_float("Yes"), trained_str_to_bool("NotTrained"), trained_str_to_bool("NotTrained"))
        self.assertEqual(result, False)

    def test_case_13(self):
        result = can_borrow("Book", age_bucket_to_int("<18"), LOAN_DAYS["Medium"],
                            fees_str_to_float("No"), trained_str_to_bool("Trained"), trained_str_to_bool("Trained"))
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
