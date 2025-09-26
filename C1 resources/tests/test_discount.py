'''
The method you are testing is:
    calculate_discount(age)

The data type of each parameter is:
- age: integer

You can assume that the calculate_discount method is already imported into this python module,
so you can call "calculate_discount" directly.

Author: Min Zhengyuan
Student ID: 34075887
'''
import unittest
from src.discount import calculate_discount

class TestCalculateDiscount(unittest.TestCase):
    """
    Test suite for calculate_discount(age).
    Partitions:
      - age <= 50          -> 0.00
      - 50 < age <= 64     -> 0.10
      - 65 <= age <= 89    -> 0.15
      - age >= 90          -> 1.00
    """

    # age <= 50
    def test_age_30(self):
        self.assertEqual(calculate_discount(30), 0.00, "Failed: Age 30 should return 0.00 discount")

    def test_age_49(self):
        self.assertEqual(calculate_discount(49), 0.00, "Failed: Age 49 should return 0.00 discount")

    def test_age_50(self):
        self.assertEqual(calculate_discount(50), 0.10, "Failed: Age 50 should return 0.10 discount")

    # 50 < age <= 64
    def test_age_51(self):
        self.assertEqual(calculate_discount(51), 0.10, "Failed: Age 51 should return 0.10 discount")

    def test_age_55(self):
        self.assertEqual(calculate_discount(55), 0.10, "Failed: Age 55 should return 0.10 discount")
    
    def test_age_64(self):
        self.assertEqual(calculate_discount(64), 0.10, "Failed: Age 64 should return 0.10 discount")

    # 65 <= age <= 89
    def test_age_65(self):
        self.assertEqual(calculate_discount(65), 0.15, "Failed: Age 65 should return 0.15 discount")

    def test_age_66(self):
        self.assertEqual(calculate_discount(66), 0.15, "Failed: Age 66 should return 0.15 discount")

    def test_age_70(self):
        self.assertEqual(calculate_discount(70), 0.15, "Failed: Age 70 should return 0.15 discount")

    def test_age_89(self):
        self.assertEqual(calculate_discount(89), 0.15, "Failed: Age 89 should return 0.15 discount")

    # age >= 90
    def test_age_90(self):
        self.assertEqual(calculate_discount(90), 1.00, "Failed: Age 90 should return 1.00 discount")

    def test_age_91(self):
        self.assertEqual(calculate_discount(91), 1.00, "Failed: Age 91 should return 1.00 discount")

    def test_age_95(self):
        self.assertEqual(calculate_discount(95), 1.00, "Failed: Age 95 should return 1.00 discount")

