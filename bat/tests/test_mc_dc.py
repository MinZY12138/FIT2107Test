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


Possible optimal sets of tests using MC/DC:

MC/DC independence pairs justification:
- A: (1, 5)
- B: (1, 3)
- C: (1, 2)

Chosen optimal set:
- {1, 2, 3, 5}

Set chosen: {1, 2, 3, 5}
'''

