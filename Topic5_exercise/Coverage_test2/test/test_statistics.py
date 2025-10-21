import unittest

from src.statistics import *

class TestStatistics(unittest.TestCase):
    def default_test(self):
        self.assertTrue(True)

    def test_sum(self):
        data = [1, 2, 3, 4]
        self.assertEqual(sum(data), 10)
        self.assertEqual(sum([]), 0)  

    def test_mean(self):
        data = [2, 4, 6, 8]
        self.assertEqual(mean(data), 5)

    def test_minimum(self):
        data = [7, 3, 5, 9, 1]
        self.assertEqual(minimum(data), 1)

    def test_maximum(self):
        data = [7, 3, 5, 9, 1]
        self.assertEqual(maximum(data), 9)

    def test_single_value(self):
        data = [5]
        self.assertEqual(minimum(data), 5)
        self.assertEqual(maximum(data), 5)
        self.assertEqual(mean(data), 5)