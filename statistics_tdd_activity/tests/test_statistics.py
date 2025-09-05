import unittest
from src import statistics as stats

class TestSum(unittest.TestCase):
    def test_sum_basic(self):
        self.assertEqual(stats.sum([1, 2, 3]), 6)

    def test_sum_with_negatives(self):
        self.assertEqual(stats.sum([5, -2, -3, 4]), 4)

    def test_sum_empty(self):
        with self.assertRaises(ValueError):
            stats.sum([])

class TestMean(unittest.TestCase):
    def test_mean_basic(self):
        self.assertAlmostEqual(stats.mean([2, 4, 6]), 4.0, places=6)

    def test_mean_decimal(self):
        self.assertAlmostEqual(stats.mean([1, 2]), 1.5, places=6)

    def test_mean_empty(self):
        with self.assertRaises(ValueError):
            stats.mean([])

class TestMinimum(unittest.TestCase):
    def test_minimum_basic(self):
        self.assertEqual(stats.minimum([3, 1, 2]), 1)

    def test_minimum_with_negatives(self):
        self.assertEqual(stats.minimum([0, -10, 5, -3]), -10)

    def test_minimum_singleton(self):
        self.assertEqual(stats.minimum([7]), 7)

    def test_minimum_empty(self):
        with self.assertRaises(ValueError):
            stats.minimum([])

class TestMaximum(unittest.TestCase):
    def test_maximum_basic(self):
        self.assertEqual(stats.maximum([3, 1, 2]), 3)

    def test_maximum_with_negatives(self):
        self.assertEqual(stats.maximum([-1, -5, -3]), -1)

    def test_maximum_singleton(self):
        self.assertEqual(stats.maximum([7]), 7)

    def test_maximum_empty(self):
        with self.assertRaises(ValueError):
            stats.maximum([])

if __name__ == "__main__":
    unittest.main()

