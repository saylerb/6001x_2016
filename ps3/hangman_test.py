import unittest

from hangman import is_word_guessed

class HangmanTest(unittest.TestCase):
    def test_word_not_guessed(self):
        secret_word = 'apple'
        letters_guessed = ['e', 'i', 'k', 'p', 'r']
        result = is_word_guessed(secret_word, letters_guessed)
        self.assertEqual(False, result)

    def test_it_returns_true_if_word_guessed_perfectly(self):
        secret_word = 'apple'
        letters_guessed = ['a', 'p', 'p', 'l', 'e']
        result = is_word_guessed(secret_word, letters_guessed)
        self.assertEqual(True, result)

    def test_it_returns_false_if_no_letters_gussed_yet(self):
        secret_word = 'apple'
        letters_guessed = []
        result = is_word_guessed(secret_word, letters_guessed)
        self.assertEqual(False, result)

    def test_it_can_handle_multiple_wrong_guesses(self):
        secret_word = 'apple'
        letters_guessed = ['a', 'p', 'k', 'p', 'r', 's', 'e', 'l']
        result = is_word_guessed(secret_word, letters_guessed)
        self.assertEqual(True, result)

    def test_the_word_durian_with_multiple_wrong_guesses(self):
        secret_word = 'durian'
        letters_guessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
        result = is_word_guessed(secret_word, letters_guessed)
        self.assertEqual(True, result)

    def test_the_word_mangosteen_with_wrong_guesses(self):
        secret_word = 'mangosteen'
        letters_guessed = ['z', 'x', 'q', 'm', 'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n']
        result = is_word_guessed(secret_word, letters_guessed)
        self.assertEqual(True, result)

if __name__ == '__main__':
    unittest.main()
