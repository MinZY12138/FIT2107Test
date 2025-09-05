import unittest
from src import statistics as stats

class TestStatistics(unittest.TestCase):
    def test_sum_basic(self):
        self.assertEqual(stats.sum([1, 2, 3]), 6)

    def test_sum_with_negatives(self):
        self.assertEqual(stats.sum([5, -2, -3, 4]), 4)

    def test_sum_empty(self):
        with self.assertRaises(ValueError):
            stats.sum([])

if __name__ == "__main__":
    unittest.main()
