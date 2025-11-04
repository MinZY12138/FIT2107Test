import unittest
from tests.patron_stub import Patron
from tests.item_stub import Item

from src.business_logic import (
    find_patron_by_name,
    find_patron_by_age,
    find_patron_by_name_and_age,
    find_item_by_id,
)


class TestFindFunctions(unittest.TestCase):
    """Unit tests for business_logic find_* helpers (one assert per test)."""

    def setUp(self):
        self.patrons = [
            Patron("Alex", 18),
            Patron("alex", 25),
            Patron("Bella", 25),
            Patron("Chris", 90),
        ]
        self.items = [Item(1), Item(2), Item(5)]

    # -------- find_patron_by_name --------
    def test_find_patron_by_name_returns_len_1_for_case_sensitive_match(self):
        result = find_patron_by_name("Alex", self.patrons)
        self.assertEqual(len(result), 1)

    def test_find_patron_by_name_no_match_returns_empty_list(self):
        self.assertEqual(find_patron_by_name("Dana", self.patrons), [])

    # -------- find_patron_by_age --------
    def test_find_patron_by_age_returns_two_25yos(self):
        result = find_patron_by_age(25, self.patrons)
        self.assertEqual(len(result), 2)

    def test_find_patron_by_age_returns_empty_when_none(self):
        self.assertEqual(find_patron_by_age(7, self.patrons), [])

    # -------- find_patron_by_name_and_age (case-insensitive on name) --------
    def test_find_patron_by_name_and_age_finds_lowercase_name(self):
        result = find_patron_by_name_and_age("alex", 18, self.patrons)
        self.assertIsNotNone(result)

    def test_find_patron_by_name_and_age_returns_none_when_absent(self):
        self.assertIsNone(find_patron_by_name_and_age("Chris", 25, self.patrons))

    # -------- find_item_by_id --------
    def test_find_item_by_id_finds_id_5(self):
        result = find_item_by_id(5, self.items)
        self.assertIsNotNone(result)

    def test_find_item_by_id_returns_none_when_missing(self):
        self.assertIsNone(find_item_by_id(999, self.items))
