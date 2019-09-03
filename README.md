# Spaceman
This is spaceman because we don't hang people here at Make School.

Flow of project

    Pick secret_word

    Enter game loop until word is guessed
    spaceman

        Check guessed letters and show which are guess and which are blank.
        get_guessed_word
            For each letter in the secret word check to see if the user has guessed it.
            If the user has guessed the letter then show the letter if not then show a space _ .

        Check if the letter guessed is in the secret word.
        is_guess_in_word
            Prompt for user input
            Check if the letter guessed is in the secret word if it is add the letter to the list
            that get_guessed_word checks against. If the letter is not in the secret word add one
            point to the users incorrect guesses. If the amount of incorrect guesses is seven
            then the the game ends.

        Check if all of the letters in the word were guessed.
        is_word_guessed
            Check if each letter in the secret word is in the user guessed letters if they are
            print the entire word then tell the user that they have won.
