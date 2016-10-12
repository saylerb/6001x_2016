import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    letters_remaining = list(set(secret_word)) # get unique letters

    for index in range(0, len(letters_guessed)):
        if len(letters_remaining) == 0:
            break
        elif letters_guessed[index] in letters_remaining:
            letters_remaining.remove(letters_guessed[index])

    if len(letters_remaining) > 0:
        return False
    else:
        return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    result = ''

    for char in secret_word:
        if char in letters_guessed:
            result += char
        else:
            result += '_'
        result += ' '

    return result.strip()

def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase

    return ''.join(sorted(list(set(alphabet).difference(letters_guessed))))

def hangman(secret_word):

    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    remaining_guesses = 8
    letters_guessed = []

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %s letters long." % len(secret_word))
    print("--------------------")

    while (not is_word_guessed(secret_word, letters_guessed)) and remaining_guesses > 0:

        print("You have %s guesses remaining!" % remaining_guesses)
        print("Available letters: %s" % get_available_letters(letters_guessed))
        current_guess = input("Please guess a letter: ")

        if current_guess in letters_guessed:
            print("Oops! You've already guessed that letter: %s" % get_guessed_word(secret_word, letters_guessed))
        elif current_guess in secret_word:
            letters_guessed.append(current_guess)
            print("Good guess: %s" % get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(current_guess)
            print("Oops! That letter is not in my word: %s" % get_guessed_word(secret_word, letters_guessed))
            remaining_guesses -= 1

        print("--------------------")

    if remaining_guesses == 0:
        print("Sorry, you ran out of guesses. The word was %s." % secret_word)
    elif is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")

if __name__ == '__main__':
    wordlist = load_words()
    secret_word = choose_word(wordlist).lower()
    hangman(secret_word)
