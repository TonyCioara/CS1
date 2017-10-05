import hangman
import pytest


def check_word_test():
    letter_array = hangman.check_word('cecereec', 'e')
    assertEqual(letter_array, [0, 1, 0, 1, 0, 1, 1, 0])
