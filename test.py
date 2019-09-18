import unittest
from spaceman import (is_word_guessed, get_guessed_word, is_guess_in_word)

class spaceman_Tests(unittest.TestCase):
    def test_is_word_guessed_true(self):
        self.assertEqual(is_word_guessed("cat", "act"), True)

    def test_is_word_guessed_more_letters(self):
        self.assertEqual(is_word_guessed("cat", "track"), True)

    def test_is_word_not_guessed(self):
        self.assertEqual(is_word_guessed("cat", "tar"), False)

    def test_is_word_guessed_no_letters(self):
        self.assertEqual(is_word_guessed("cat", ""), False)

    def test_get_guessed_word_true(self):
        self.assertEqual(get_guessed_word("cat", "act"), "cat")

    def test_get_guessed_word_no_letters(self):
        self.assertEqual(get_guessed_word("cat", ""), "_ _ _ ")

    def test_get_guessed_word_no_right_letters(self):
        self.assertEqual(get_guessed_word("cat", "done"), "_ _ _ ")

    def test_get_guessed_word_multiletter(self):
        self.assertEqual(get_guessed_word("mississippi", "s"), "_ _ ss_ ss_ _ _ _ ")

    def test_is_guess_in_word_true(self):
        self.assertEqual(is_guess_in_word("t", "fact"), "t")

    def test_is_guess_in_word_false(self):
        self.assertEqual(is_guess_in_word("r", "fact"), "~")

    def test_is_guess_in_word_non_option_upper(self):
        self.assertEqual(is_guess_in_word("T", "fact"), "t")

    def test_is_guess_in_word_option_upper(self):
        self.assertEqual(is_guess_in_word("Q", "fact"), "Q")


if __name__ == '__main__':
    unittest.main()
