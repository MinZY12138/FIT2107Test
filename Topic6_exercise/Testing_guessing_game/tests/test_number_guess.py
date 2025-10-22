import unittest
from unittest.mock import patch
from src.guessing_game import *

class TestGuessingGame(unittest.TestCase):

    def test_high_low_correct(self):
        self.assertTrue(guess_too_high(80, 60))
        self.assertFalse(guess_too_high(50, 70))
        self.assertTrue(guess_too_low(30, 50))
        self.assertFalse(guess_too_low(60, 50))
        self.assertTrue(guess_correct(42, 42))
        self.assertFalse(guess_correct(41, 42))

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["25"])
    def test_get_guess_valid_once(self, mock_input, mock_print):
        value = get_guess()
        self.assertEqual(value, 25)
        mock_print.assert_any_call("Enter a number between 0 and 100: ", end='')

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["-1", "10"])
    def test_get_guess_out_of_range_then_ok(self, mock_input, mock_print):
        value = get_guess()
        self.assertEqual(value, 10)
        self.assertGreaterEqual(mock_print.call_count, 1)


    @patch("src.guessing_game.select_answer", return_value=42)
    @patch("builtins.input", side_effect=["42", "n"])
    def test_play_game_hit_first_time(self, mock_input, _mock_answer):

        play_game()


    @patch("builtins.print")
    @patch("src.guessing_game.select_answer", return_value=90)
    @patch("builtins.input", side_effect=(["0"] * 10) + ["n"])
    def test_play_game_too_many(self, mock_input, _mock_answer, mock_print):
        play_game()
        calls = [c.args[0] for c in mock_print.call_args_list if c.args]
        self.assertIn("Too many guesses! Sorry.", calls)
        self.assertIn("Play again? Enter y for yes, or anything else for no: ", calls)




