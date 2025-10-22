import unittest
from unittest import mock
import src.number_guess as number_guess

class TestNumberGuess60(unittest.TestCase):
    def test_guess_too_high_true(self):
        self.assertTrue(number_guess.guess_too_high(80, 50))

    def test_guess_too_low_true(self):
        self.assertTrue(number_guess.guess_too_low(20, 50))

    def test_guess_correct_true(self):
        self.assertTrue(number_guess.guess_correct(50, 50))

    @mock.patch("builtins.input", return_value="5")
    def test_get_guess_in_range(self, inp):
        self.assertEqual(5, number_guess.get_guess())

    @mock.patch("builtins.input", side_effect=["150", "12"])
    def test_get_guess_out_then_in(self, inp):
        self.assertEqual(12, number_guess.get_guess())

    @mock.patch("random.randint", return_value=42)
    def test_select_answer_fixed(self, rint):
        self.assertEqual(42, number_guess.select_answer())
        rint.assert_called_once_with(0, 100)

    @mock.patch("builtins.input", side_effect=["41", "42", "n"])
    @mock.patch("random.randint", return_value=42)
    def test_play_game_quick_win_then_quit(self, rint, inp):
        number_guess.play_game()
        self.assertTrue(True)




