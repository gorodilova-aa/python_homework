def make_hangman(secret_word):

    # empty array
    guesses = []

    def hangman_closure(letter):
        if letter.lower() not in guesses:
            guesses.append(letter.lower())
        
        word_guessed_letters =  "".join(
            [x if x.lower() in guesses else "_" for x in secret_word]
        )  
        print(word_guessed_letters)

        # check if all guessed
        all_guessed = True
        for x in word_guessed_letters:
            if x.lower() == "_": 
                all_guessed = False
        return all_guessed

    return hangman_closure

# game
secret_word = input("Enter the secret_word: ")

hangman_game = make_hangman(secret_word)

end_game = False
while not end_game:
    letter_guess = input("Input a letter: ") 
    end_game = hangman_game(letter_guess)


