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

    
    @patch("src.bat_ui.user_input.read_integer_range", return_value=1)
    def test_choice_1_goes_to_loan_item(self, _):
        """Valid input '1' should navigate to the LOAN ITEM screen."""
        self.ui = BatUI(data_manager=None)
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "LOAN ITEM")

    @patch("src.bat_ui.user_input.read_integer_range", return_value=2)
    def test_choice_2_goes_to_return_item(self, _):
        """Valid input '2' should navigate to the RETURN ITEM screen."""
        self.ui = BatUI(data_manager=None)
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "RETURN ITEM")

    @patch("src.bat_ui.user_input.read_integer_range", return_value=3)
    def test_choice_3_goes_to_search_for_patron(self, _):
        """Valid input '3' should navigate to the SEARCH FOR PATRON screen."""
        self.ui = BatUI(data_manager=None)
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @patch("src.bat_ui.user_input.read_integer_range", return_value=4)
    def test_choice_4_goes_to_register_patron(self, _):
        """Valid input '4' should navigate to the REGISTER PATRON screen."""
        self.ui = BatUI(data_manager=None)
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "REGISTER PATRON")

    @patch("src.bat_ui.user_input.read_integer_range", return_value=5)
    def test_choice_5_goes_to_access_makerspace(self, _):
        """Valid input '5' should navigate to the ACCESS MAKERSPACE screen."""
        self.ui = BatUI(data_manager=None)
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "ACCESS MAKERSPACE")

    @patch("src.bat_ui.user_input.read_integer_range", return_value=6)
    def test_choice_6_goes_to_quit(self, _):
        """Valid input '6' should navigate to the QUIT screen."""
        self.ui = BatUI(data_manager=None)
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "QUIT")


    # Invalid input test

    @patch("builtins.input", side_effect=["9", "1"])
    def test_invalid_then_valid_reprompts_and_moves(self, mock_input):
        """
        First input '9' is invalid
        The user is asked again and enters '1'.
        The UI should finally move to the LOAN ITEM screen.
        """
        self.ui = BatUI(data_manager=None)
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "LOAN ITEM")

    @patch("builtins.input", side_effect=["-1", "3"])
    def test_invalid_negative_then_valid(self, mock_input):
        """
        First input '-1' is invalid
        The user is asked again and enters '3'.
        The UI should finally move to the SEARCH FOR PATRON screen.
        """
        self.ui = BatUI(data_manager=None)
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @patch("builtins.input", side_effect=["abc", "1"])
    def test_invalid_string_then_valid(self, mock_input):
        """
        First input 'abc' is invalid
        The user is asked again and enters '1'.
        The UI should finally move to the LOAN ITEM screen.
        """
        self.ui = BatUI(data_manager=None)
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "LOAN ITEM")

    @patch("builtins.input", side_effect=["1.5", "2"])
    def test_invalid_float_then_valid(self, mock_input):
        """
        First input '1.5' is invalid
        The user is asked again and enters '2'.
        The UI should finally move to the RETURN ITEM screen.
        """
        self.ui = BatUI(data_manager=None)
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "RETURN ITEM")