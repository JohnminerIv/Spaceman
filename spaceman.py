import random


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use
    as the secret word from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been
    guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been
        guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in
        letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter
    # is not in lettersGuessed
    build_word = ""
    for letter in secret_word:
        in_word = letter in letters_guessed
        if in_word is True:
            build_word = build_word + letter
        else:
            build_word = build_word + "_ "
    if build_word == secret_word:
        return True
    else:
        return False
    pass


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far
    in the secret word and underscores for letters that have not been guessed
    yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been
        guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user
        has guessed correctly, the string should contain the letter at the
        correct position.  For letters in the word that the user has not yet
        guessed, shown an _ (underscore) instead.
    '''
    # TODO: Loop through the letters in secret word and build a string that
    # shows the letters that have been guessed correctly so far that are saved
    # in letters_guessed and underscores for the letters that have not been
    # guessed yet
    build_word = ""
    for letter in secret_word:
        in_word = letter in letters_guessed
        if in_word is True:
            build_word = build_word + letter
        else:
            build_word = build_word + "_ "
    return build_word

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    # TODO: check if the letter guess is in the secret word
    guessed_letter = guess
    if guessed_letter == "Q":
        return guessed_letter
    elif guessed_letter == "N":
        return guessed_letter
    guessed_letter = guessed_letter.lower()
    letters_guessed = ""
    for letter in secret_word:
        is_in_word = guessed_letter == letter
        if is_in_word is True:
            letters_guessed = letters_guessed + guessed_letter + "0"
        else:
            if "W" not in letters_guessed:
                letters_guessed += "W"

    return letters_guessed
    pass


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the
    command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    # TODO: show the player information about the game according to the
    # project spec

    # TODO: Ask the player to guess one letter per round and check that it is
    # only one letter

    # TODO: Check if the guessed letter is in the secret or not and give the
    # player feedback

    # TODO: show the guessed word so far

    # TODO: check if the game has been won or lost
    letters = ""
    game_state = "playing"
    wrong_answers = 0
    while game_state == "playing":
        print("\033[H\033[J")
        # print(letters)
        print(get_guessed_word(secret_word, letters))
        letters = letters + is_guess_in_word(input(F"""You get 7 wrong answers,
you have alreday answered wrong {wrong_answers} time(s)
Type Q to quit or
Type N to get a new word or
Please guess a letter: """), secret_word)
        if "Q" in letters:
            letters = ""
            game_state = "quit"
        elif "N" in letters:
            letters = ""
            wrong_answers = 0
            secret_word = load_word()
        elif "W" in letters and "0" in letters:
            letters2 = ""
            for letter in letters:
                if letter != "W" and letter != "0":
                    letters2 += letter
            letters = letters2
        elif "W" in letters:
            wrong_answers += 1
            letters2 = ""
            for letter in letters:
                if letter != "W":
                    letters2 += letter
            letters = letters2
            if wrong_answers == 7:
                print("Oh no, you have killed the spaceman!")
                game_state = "pause"
        else:
            return
        if is_word_guessed(secret_word, letters) is True:
            print("You have saved the spaceman!")
            game_state = "pause"


# These function calls that will start the game
secret_word = load_word()
spaceman(load_word())
