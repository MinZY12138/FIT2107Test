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
    Interpreted partitions from your design:
      - age < 50          -> 0.00
      - 50 <= age <= 64   -> 0.10
      - 65 <= age <= 89   -> 0.15
      - age >= 90         -> 1.00
    """

    def test_ep_bva(self):
        """Combined EP + BVA tests for calculate_discount(age)."""
        cases = [
            
            (30, 0.00),
            (49, 0.00),
            (50, 0.10),
            (51, 0.10),
            (55, 0.10),
            (64, 0.10),
            (65, 0.15),
            (66, 0.15),
            (70, 0.15),
            (89, 0.15),
            (90, 1.00),
            (91, 1.00),
            (95, 1.00),
        ]
        for age, expected in cases:
            with self.subTest(age=age):
                result = calculate_discount(age)
                self.assertAlmostEqual(result, expected, places=2)


if __name__ == "__main__":
    unittest.main()