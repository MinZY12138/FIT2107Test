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

    
    @patch("builtins.input")
    def test_choice_1_goes_to_loan_item(self, inp):
        """Valid input '1' should navigate to the LOAN ITEM screen."""
        inp.return_value = "1"
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._loan_item)

    @patch("builtins.input")
    def test_choice_2_goes_to_return_item(self, inp):
        """Valid input '2' should navigate to the RETURN ITEM screen."""
        inp.return_value = "2"
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._return_item)

    @patch("builtins.input")
    def test_choice_3_goes_to_search_for_patron(self, inp):
        """Valid input '3' should navigate to the SEARCH FOR PATRON screen."""
        inp.return_value = "3"
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._search_for_patron)

    @patch("builtins.input")
    def test_choice_4_goes_to_register_patron(self, inp):
        """Valid input '4' should navigate to the REGISTER PATRON screen."""
        inp.return_value = "4"
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._register_patron)

    @patch("builtins.input")
    def test_choice_5_goes_to_access_makerspace(self, inp):
        """Valid input '5' should navigate to the ACCESS MAKERSPACE screen."""
        inp.return_value = "5"
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._access_makerspace)

    @patch("builtins.input")
    def test_choice_6_goes_to_quit(self, inp):
        """Valid input '6' should navigate to the QUIT screen."""
        inp.return_value = "6"
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._quit)


    # Invalid input test

    @patch("builtins.input")
    def test_invalid_then_valid_reprompts_and_moves(self, inp):
        """
        First input '9' is invalid
        The user is asked again and enters '1'.
        The UI should finally move to the LOAN ITEM screen.
        """
        inp.side_effect = ["9", "1"]
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._loan_item)

    @patch("builtins.input")
    def test_invalid_negative_then_valid(self, inp):
        """
        First input '-1' is invalid
        The user is asked again and enters '3'.
        The UI should finally move to the SEARCH FOR PATRON screen.
        """
        inp.side_effect = ["-1", "3"]
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._search_for_patron)

    @patch("builtins.input")
    def test_invalid_string_then_valid(self, inp):
        """
        First input 'abc' is invalid
        The user is asked again and enters '1'.
        The UI should finally move to the LOAN ITEM screen.
        """
        inp.side_effect = ["abc", "1"]
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._loan_item)


    @patch("builtins.input")
    def test_invalid_float_then_valid(self, inp):
        """
        First input '1.5' is invalid
        The user is asked again and enters '2'.
        The UI should finally move to the RETURN ITEM screen.
        """
        inp.side_effect = ["1.5", "2"]
        next_screen = self.ui._main_menu()
        self.assertIs(next_screen, self.ui._return_item)
