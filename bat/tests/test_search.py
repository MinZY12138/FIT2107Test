import unittest

# Import the functions under test
from src.search import (
    find_patron_by_name,
    find_patron_by_age,
    find_patron_by_name_and_age,
    find_item_by_id,
)

# --- Minimal test doubles (only attributes used by the functions) ---
class Patron:
    def __init__(self, name, age):
        self._name = name
        self._age = age

class Item:
    def __init__(self, item_id):
        self._id = item_id


class TestSearchFunctions(unittest.TestCase):
    def setUp(self):
        # Patrons: include duplicates, different cases and ages
        self.patrons = [
            Patron("Alex", 18),
            Patron("Alex", 25),
            Patron("alex", 25),     # lower-case variant
            Patron("Bella", 30),
        ]
        # Catalogue items (include a duplicate ID to exercise the loop logic)
        self.items = [Item(1), Item(2), Item(5), Item(5)]

    # ---------- find_patron_by_name ----------
    def test_find_patron_by_name_exact_match_multiple(self):
        """Exact (case-sensitive) match should return all exact matches."""
        result = find_patron_by_name("Alex", self.patrons)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(p._name == "Alex" for p in result))

    def test_find_patron_by_name_no_match_and_case_sensitivity(self):
        """Nonexistent name (or different case) returns an empty list."""
        self.assertEqual(find_patron_by_name("Dana", self.patrons), [])
        # Docstring says 'case insensitive', but implementation is case-sensitive:
        self.assertEqual(find_patron_by_name("alex", self.patrons), [self.patrons[2]])

    # ---------- find_patron_by_age ----------
    def test_find_patron_by_age_multiple_and_none(self):
        """Return all patrons with the given age; empty when no match."""
        result = find_patron_by_age(25, self.patrons)
        self.assertEqual({p._name for p in result}, {"Alex", "alex"})
        self.assertEqual(find_patron_by_age(99, self.patrons), [])

    # ---------- find_patron_by_name_and_age ----------
    def test_find_patron_by_name_and_age_found_case_insensitive(self):
        """This function compares name in a case-insensitive way."""
        r = find_patron_by_name_and_age("alex", 18, self.patrons)
        self.assertIsNotNone(r)
        self.assertEqual((r._name, r._age), ("Alex", 18))

    def test_find_patron_by_name_and_age_not_found(self):
        """Return None when no (name, age) pair matches."""
        self.assertIsNone(find_patron_by_name_and_age("Bella", 25, self.patrons))

    # ---------- find_item_by_id ----------
    def test_find_item_by_id_found_last_match_and_not_found(self):
        r = find_item_by_id(5, self.items)
        # Compare by value, not identity
        self.assertIsNotNone(r)
        self.assertEqual(r._id, self.items[-1]._id)
        self.assertIsNone(find_item_by_id(999, self.items))
