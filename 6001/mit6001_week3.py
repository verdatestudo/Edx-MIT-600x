'''
MIT6001 edX - week3 problem set.

Hangman game.

Last Updated: 2016-Oct-27
First Created: 2016-Oct-26
Python 3.5
Chris
'''

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words_week3.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # checks if set(secretWord) is a subset of set(lettersGuessed) - if so user has checked (at minimum) all the letters in the secret word.
    return set(secretWord) <= set(lettersGuessed)

    # OR can use this method
    # return all(letter in lettersGuessed for letter in secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # use list comp to show either the letter or _ (depending on if the letter has been guessed) for each letter in secretWord
    # then use join to return it as a string
    return ''.join([letter if letter in lettersGuessed else ' _ ' for letter in secretWord])


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    return ''.join([letter for letter in string.ascii_lowercase if letter not in lettersGuessed])

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lives_left = 8
    lettersGuessed = set([])

    print('Welcome to the game, Hangman! \nI am thinking of a word that is %d letters long.' %(len(secretWord)))

    while lives_left > 0 and not isWordGuessed(secretWord, lettersGuessed):

        feedback = ['Good guess: ', 'Oops! That letter is not in my word: ', 'Oops! You\'ve already guessed that letter: ', 'Oops! That isn\'t a letter.']

        print('-------------')
        print('You have %d guesses left.' %(lives_left))
        print('Available letters: ', getAvailableLetters(lettersGuessed))

        user_guess = input('Please guess a letter: ').lower()
        if user_guess in getAvailableLetters(lettersGuessed): # if valid guess
            lettersGuessed.update(user_guess)
            if user_guess in secretWord: # if good guess
                result = 0
            else: # if bad guess, lose a life
                lives_left -= 1
                result = 1
        elif user_guess in lettersGuessed:
            result = 2
        else:
            result = 3

        print(feedback[result], getGuessedWord(secretWord, lettersGuessed))

    if lives_left == 0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was %s.' %(secretWord))

    if isWordGuessed(secretWord, lettersGuessed):
        print('-------------')
        print('Congratulations, you won!')

#hangman('test')

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
