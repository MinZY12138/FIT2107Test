import unittest
from unittest.mock import patch

from src.bat_ui import BatUI

class TestBatUI_MainMenu(unittest.TestCase):
    """
    Tests for the _main_menu method in BatUI using mocking.
    """

    def setUp(self):
        self.ui = BatUI(data_manager=None)

    # Valid input tests

    
    @patch("builtins.input", side_effect=["1"])
    def test_choice_1_goes_to_loan_item(self, _):
        """Valid input '1' should navigate to the LOAN ITEM screen."""
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._loan_item)
        self.ui._current_screen = next_screen
        self.assertEqual(self.ui.get_current_screen(), "LOAN ITEM")

    @patch("builtins.input", side_effect=["2"])
    def test_choice_2_goes_to_return_item(self, _):
        """Valid input '2' should navigate to the RETURN ITEM screen."""
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._return_item)
        self.ui._current_screen = next_screen
        self.assertEqual(self.ui.get_current_screen(), "RETURN ITEM")

    @patch("builtins.input", side_effect=["3"])
    def test_choice_3_goes_to_search_for_patron(self, _):
        """Valid input '3' should navigate to the SEARCH FOR PATRON screen."""
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._search_for_patron)
        self.ui._current_screen = next_screen
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @patch("builtins.input", side_effect=["4"])
    def test_choice_4_goes_to_register_patron(self, _):
        """Valid input '4' should navigate to the REGISTER PATRON screen."""
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._register_patron)
        self.ui._current_screen = next_screen
        self.assertEqual(self.ui.get_current_screen(), "REGISTER PATRON")

    @patch("builtins.input", side_effect=["5"])
    def test_choice_5_goes_to_access_makerspace(self, _):
        """Valid input '5' should navigate to the ACCESS MAKERSPACE screen."""
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._access_makerspace)
        self.ui._current_screen = next_screen
        self.assertEqual(self.ui.get_current_screen(), "ACCESS MAKERSPACE")

    @patch("builtins.input", side_effect=["6"])
    def test_choice_6_goes_to_quit(self, _):
        """Valid input '6' should navigate to the QUIT screen."""
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._quit)
        self.ui._current_screen = next_screen
        self.assertEqual(self.ui.get_current_screen(), "QUIT")

    # Invalid input test
    
    @patch("builtins.input", side_effect=["9", "1"])
    def test_invalid_then_valid_reprompts_and_moves(self, _):
        """
        First input '9' is invalid (outside 1–6 range).
        The user is asked again and enters '1'.
        The UI should finally move to the LOAN ITEM screen.
        """
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._loan_item)
        self.ui._current_screen = next_screen
        self.assertEqual(self.ui.get_current_screen(), "LOAN ITEM")