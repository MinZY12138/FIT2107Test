'''
The method you are testing is: pairwise testing
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


# ---------- Helpers to convert spreadsheet-style values to function parameter types ----------
LOAN_DAYS = {"Short": 7, "Medium": 14, "Long": 28}

def fees_str_to_float(outstanding_fees: str) -> float:
    return 10.0 if str(outstanding_fees).strip().lower() == "yes" else 0.0

def trained_str_to_bool(training: str) -> bool:
    return str(training).strip().lower() == "trained"

def age_bucket_to_int(patron_age: str) -> int:
    s = str(patron_age).strip()
    if s.startswith("<"):                 # "<18"
        return 17
    if s.startswith(">=") or s.startswith("=>"):   # ">=90"
        return 90
    if "-" in s:                          # "18-89"
        return 30                         # representative value
    try:
        return int(s)
    except Exception:
        return 30


class TestCanBorrow(unittest.TestCase):
    def test_all_pairwise_cases(self):
        # (item_type, patron_age, length_of_loan, outstanding_fees, gardening_training, carpentry_training, expected)
        cases = [
            ("CarpentryTool", "<18",  "Short",  "Yes", "Trained",    "NotTrained", False),
            ("GardeningTool", "<18",  "Long",   "No",  "NotTrained", "Trained",    False),
            ("Book",         ">=90", "Medium", "Yes", "Trained",    "Trained",    True),
            ("Book",         "18-89","Medium", "No",  "NotTrained", "NotTrained", True),
            ("Book",         ">=90", "Long",   "No",  "Trained",    "NotTrained", True),
            ("CarpentryTool","18-89","Short",  "Yes", "NotTrained", "Trained",    False),
            ("CarpentryTool",">=90", "Long",   "No",  "NotTrained", "Trained",    False),
            ("Book",         ">=90", "Short",  "No",  "Trained",    "Trained",    True),
            ("CarpentryTool","<18",  "Medium", "No",  "Trained",    "Trained",    False),
            ("GardeningTool",">=90", "Medium", "Yes", "Trained",    "NotTrained", False),
            ("GardeningTool","18-89","Long",   "Yes", "Trained",    "NotTrained", False),
            ("GardeningTool","<18",  "Short",  "Yes", "NotTrained", "NotTrained", False),
            ("Book",         "<18",  "Medium", "No",  "Trained",    "Trained",    True),
        ]

        for item_type, patron_age, length_of_loan, outstanding_fees, gardening_training, carpentry_training, expected in cases:
            with self.subTest(item_type=item_type, age=patron_age, loan=length_of_loan, fees=outstanding_fees):
                result = can_borrow(
                    item_type,
                    age_bucket_to_int(patron_age),
                    LOAN_DAYS[length_of_loan],
                    fees_str_to_float(outstanding_fees),
                    trained_str_to_bool(gardening_training),
                    trained_str_to_bool(carpentry_training)
                )
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
