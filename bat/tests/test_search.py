import unittest
from src.search import (
    find_patron_by_name,
    find_patron_by_age,
    find_patron_by_name_and_age,
    find_item_by_id,
)

# --- Minimal test doubles (only attributes that are used by the functions) ---
class Patron:
    def __init__(self, name, age):
        self._name = name
        self._age = age


class Item:
    def __init__(self, item_id):
        self._id = item_id


class TestSearchFunctions(unittest.TestCase):
    def setUp(self):
        # Patrons include duplicates and case differences
        self.patrons = [
            Patron("Alex", 18),
            Patron("Alex", 25),
            Patron("alex", 25),
            Patron("Bella", 30),
        ]
        # Items include two with same ID to test last-match logic
        self.items = [Item(1), Item(2), Item(5), Item(5)]

    # ---------- find_patron_by_name ----------
    def test_find_patron_by_name_exact_match_multiple(self):
        """Should return all exact (case-sensitive) matches."""
        result = find_patron_by_name("Alex", self.patrons)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(p._name == "Alex" for p in result))

    def test_find_patron_by_name_no_match_and_case_sensitivity(self):
        """Nonexistent name returns [], and implementation is case-sensitive."""
        self.assertEqual(find_patron_by_name("Dana", self.patrons), [])
        result = find_patron_by_name("alex", self.patrons)
        self.assertEqual([p._name for p in result], ["alex"])

    # ---------- find_patron_by_age ----------
    def test_find_patron_by_age_multiple_and_none(self):
        """Return all patrons with the given age; empty when no match."""
        result = find_patron_by_age(25, self.patrons)
        self.assertEqual({p._name for p in result}, {"Alex", "alex"})
        self.assertEqual(find_patron_by_age(99, self.patrons), [])

    # ---------- find_patron_by_name_and_age ----------
    def test_find_patron_by_name_and_age_found_case_insensitive(self):
        """Should match regardless of case because .lower() is used."""
        r = find_patron_by_name_and_age("alex", 18, self.patrons)
        self.assertIsNotNone(r)
        self.assertEqual((r._name, r._age), ("Alex", 18))

    def test_find_patron_by_name_and_age_not_found(self):
        """Return None when no (name, age) pair exists."""
        self.assertIsNone(find_patron_by_name_and_age("Chris", 25, self.patrons))
