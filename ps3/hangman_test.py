import unittest

from hangman import is_word_guessed

class HangmanTest(unittest.TestCase):
    #@unittest.skip("skipping")
    def test_it_returns_false_if_word_not_guessed(self):
        secret_word = 'apple'
        letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
        result = is_word_guessed(secret_word, letters_guessed)
        self.assertEqual(False, result)

    def test_it_returns_true_if_word_guessed(self):
        secret_word = 'apple'
        letters_guessed = ['a', 'p', 'p', 'l', 'e']
        result = is_word_guessed(secret_word, letters_guessed)
        self.assertEqual(True, result)

if __name__ == '__main__':
    unittest.main()
