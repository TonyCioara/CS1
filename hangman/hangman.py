import random
import string

guesses_left = 6
guesses_arr = []
alphabet = list(string.ascii_lowercase)


def load_word():
    f = open('words.txt', 'r')
    wordsList = f.readlines()
    f.close()

    wordsList = wordsList[0].split(' ')
    secretWord = random.choice(wordsList)
    return secretWord


def check_word(secret_word, letter):
    letter_match_arr = []
    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            letter_match_arr.append(1)
        else:
            letter_match_arr.append(0)
    return letter_match_arr


def get_input(guessed_word):
    global guesses_left
    global guesses_arr
    global alphabet
    print(" ")
    print(*guessed_word)
    print("You have", guesses_left, "guesses left")
    to_return = 0
    while to_return == 0:
        print("Guesses made:", *guesses_arr)
        new_guess = input("Guess a new letter: ")
        if len(new_guess) > 1:
            print("\n That is more than one letter!")
        elif new_guess not in alphabet:
            print("\n That was not a valid character")
        elif new_guess in guesses_arr:
            print("\n That letter was already guessed!")
        else:
            to_return = 1
    return new_guess


def append_new_letters(guessed_word, letter_match_arr, new_guess):
    global guesses_left
    was_wrong = True
    for i in range(0, len(letter_match_arr)):
        if letter_match_arr[i] == 1:
            guessed_word[i] = new_guess
            was_wrong = False

    if was_wrong is True:
        guesses_left -= 1
    guesses_arr.append(new_guess)
    return guessed_word


def restart():
    global guesses_left
    global guesses_arr
    to_restart = input("Play again? y/n: ")
    if to_restart == "y":
        guesses_left = 6
        guesses_arr = []
        hangman(load_word())
    else:
        return


def hangman(secret_word):
    global guesses_left
    global guesses_arr
    list(secret_word)
    guessed_word = []

    for i in range(0, len(secret_word)):
        guessed_word.append('_')

    while guesses_left > 0:
        new_guess = get_input(guessed_word)
        letter_match_arr = check_word(secret_word, new_guess)
        append_new_letters(guessed_word, letter_match_arr, new_guess)
        if '_' in guessed_word:
            pass
        else:
            print("YOU WIN! The word was", secret_word)
            restart()

    print("YOU LOST! :() The word was", secret_word)
    restart()


secretWord = load_word()
hangman(load_word())
