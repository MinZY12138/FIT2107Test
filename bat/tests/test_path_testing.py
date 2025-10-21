import unittest

from src.business_logic import can_use_makerspace


'''
Feasible paths:
1: 148->150->151->153->154->161->164
2: 148->150->151->153->155->156->161->164
3: 148->150->151->153->155->157->158->159->161->164
4: 148->150->151->153->155->157->158->159->161->162->164

'''

class Test_CanUseMakerspace(unittest.TestCase):

    # Test for 1: 148->150->151->153->154->161->164
    def test_path1_error_patron_type(self):
        result = can_use_makerspace(
            patron_age=-1,
            outstanding_fees=0.0,
            makerspace_training=True
        )
        self.assertFalse(result)

    # Test for 2: 148->150->151->153->155->156->161->164
    def test_path2_minor_or_elderly(self):
        result = can_use_makerspace(
            patron_age=17,
            outstanding_fees=0.0,
            makerspace_training=True
        )
        self.assertFalse(result)

    # Test for 3: 148->150->151->153->155->157->158->159->161->164
    def test_path3_adult_training_true_fees_positive(self):
        result = can_use_makerspace(
            patron_age=30,
            outstanding_fees=10.0,
            makerspace_training=True
        )
        self.assertFalse(result)

    # Test for 4: 148->150->151->153->155->157->158->159->161->162->164
    def test_path4_adult_training_true_no_fees(self):
        result = can_use_makerspace(
            patron_age=30,
            outstanding_fees=0.0,
            makerspace_training=True
        )
        self.assertTrue(result)