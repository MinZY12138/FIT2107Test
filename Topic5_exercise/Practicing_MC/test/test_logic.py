import unittest

from src.my_code import method_to_test

'''
Possible tests:
1: A=F, B=F, C=F, D=F, Outcome=F
2: A=F, B=F, C=F, D=T, Outcome=F
3: A=F, B=F, C=T, D=F, Outcome=F
4: A=F, B=F, C=T, D=T, Outcome=F
5: A=F, B=T, C=F, D=F, Outcome=F
6: A=F, B=T, C=F, D=T, Outcome=F
7: A=F, B=T, C=T, D=F, Outcome=F
8: A=F, B=T, C=T, D=T, Outcome=F
9: A=T, B=F, C=F, D=F, Outcome=F
10: A=T, B=F, C=F, D=T, Outcome=F
11: A=T, B=F, C=T, D=F, Outcome=F
12: A=T, B=F, C=T, D=T, Outcome=T
13: A=T, B=T, C=F, D=F, Outcome=F
14: A=T, B=T, C=F, D=T, Outcome=T
15: A=T, B=T, C=T, D=F, Outcome=F
16: A=T, B=T, C=T, D=T, Outcome=T

Chosen optimal MC/DC set (different from the sample above):
- 6, 10, 11, 12, 14

Rationale (independence pairs):
- A: (6 → F) vs (14 → T) with only A toggled via using 10/12 as anchors
- B: (10 → F) vs (14 → T)
- C: (11 → F) vs (12 → T)
- D: (10/11 → F) vs (12/14 → T)
'''

class TestMyCodeAlt(unittest.TestCase):
    # 6: A=F, B=T, C=F, D=T → F
    def test_f_t_f_t(self):
        self.assertFalse(method_to_test(False, True, False, True))

    # 10: A=T, B=F, C=F, D=T → F
    def test_t_f_f_t(self):
        self.assertFalse(method_to_test(True, False, False, True))

    # 11: A=T, B=F, C=T, D=F → F
    def test_t_f_t_f(self):
        self.assertFalse(method_to_test(True, False, True, False))

    # 12: A=T, B=F, C=T, D=T → T
    def test_t_f_t_t(self):
        self.assertTrue(method_to_test(True, False, True, True))

    # 14: A=T, B=T, C=F, D=T → T
    def test_t_t_f_t(self):
        self.assertTrue(method_to_test(True, True, False, True))