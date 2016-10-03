import unittest

from hangman import is_word_guessed, get_guessed_word

class IsWordGuessedTest(unittest.TestCase):
    def test_word_not_guessed(self):
        secret_word = 'pizza'
        letters_guessed = ['e', 'a', 'k', 'i', 'r']
        result = is_word_guessed(secret_word, letters_guessed)
        self.assertEqual(False, result)

    def test_it_returns_true_if_word_guessed_perfectly(self):
        secret_word = 'kale'
        letters_guessed = ['k', 'a', 'l', 'e']
        result = is_word_guessed(secret_word, letters_guessed)
        self.assertEqual(True, result)

    def test_it_returns_false_if_no_letters_gussed_yet(self):
        secret_word = 'salad'
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

class GetWordGuessedTest(unittest.TestCase):
    def test_word_that_has_no_letters_guessed_yet(self):
        secret_word = 'grape'
        letters_guessed = []
        result = get_guessed_word(secret_word, letters_guessed)
        self.assertEqual('_ _ _ _ _', result)

    def test_word_that_has_one_letter_guessed(self):
        secret_word = 'banana'
        letters_guessed = ['a']
        result = get_guessed_word(secret_word, letters_guessed)
        self.assertEqual('_ a _ a _ a', result)

    def test_word_that_has_all_letters_guessed(self):
        secret_word = 'tact'
        letters_guessed = ['t', 'a', 'c', 't']
        result = get_guessed_word(secret_word, letters_guessed)
        self.assertEqual('t a c t', result)

if __name__ == '__main__':
    unittest.main()
