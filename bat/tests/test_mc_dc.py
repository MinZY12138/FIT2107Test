import unittest

from src.business_logic import can_borrow_carpentry_tool

'''
Possible tests:
1: A=F, B=F, C=F, Outcome=F
2: A=F, B=F, C=T, Outcome=T
3: A=F, B=T, C=F, Outcome=T
4: A=F, B=T, C=T, Outcome=T
5: A=T, B=F, C=F, Outcome=T
6: A=T, B=F, C=T, Outcome=T
7: A=T, B=T, C=F, Outcome=T
8: A=T, B=T, C=T, Outcome=T


Possible optimal sets of tests using MC/DC: {1, 2, 3, 5}

MC/DC independence pairs justification:
- A: (1, 5)
- B: (1, 3)
- C: (1, 2)


Set chosen: {1, 2, 3, 5}
'''

class TestCanBorrowCarpentryTool(unittest.TestCase):
    # Test 1: A=F, B=F, C=F → Outcome=F
    def test_no_fees_adult_normal_age(self):
        result = can_borrow_carpentry_tool(
            patron_age=30,
            length_of_loan=7,
            outstanding_fees=0.0,
            carpentry_tool_training=True
        )
        self.assertTrue(result)  

    # Test 2: A=F, B=F, C=T → Outcome=T
    def test_elderly_no_fees(self):
        result = can_borrow_carpentry_tool(
            patron_age=90,
            length_of_loan=7,
            outstanding_fees=0.0,
            carpentry_tool_training=True
        )
        self.assertFalse(result)

    # Test 3: A=F, B=T, C=F → Outcome=T
    def test_underage_no_fees(self):
        result = can_borrow_carpentry_tool(
            patron_age=17,
            length_of_loan=7,
            outstanding_fees=0.0,
            carpentry_tool_training=True
        )
        self.assertFalse(result)

    # Test 5: A=T, B=F, C=F → Outcome=T
    def test_fees_due_adult(self):
        result = can_borrow_carpentry_tool(
            patron_age=30,
            length_of_loan=7,
            outstanding_fees=50.0,
            carpentry_tool_training=True
        )
        self.assertFalse(result)