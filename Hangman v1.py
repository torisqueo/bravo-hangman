from Hang_Class import Inc

def hangman():
    # setup
    secret_word = list("twig")
    guess_word = list(str(" ") * (len(secret_word)))

    # hangman body
    lig = ["left arm", "right arm", "left leg", "right leg", "torso", "head"]
    wrong = [Inc(0, "none"),
             Inc(1, lig[0]),
             Inc(2, lig[1]),
             Inc(3, lig[2]),
             Inc(4, lig[3]),
             Inc(5, lig[4]),
             Inc(6, lig[5]),
             ]

    # guessing
    guess_count = 0
    total_guess = (len(lig))

    # play on
    while guess_word != secret_word and guess_count != total_guess:
        guess = input("\nEnter a letter: ")
        guess = guess.lower()

        if guess in secret_word:
            guess_word[secret_word.index(guess)] = guess
            print(guess_word)

        elif guess not in secret_word:
            guess_count += 1
            if guess_count < (total_guess - 1):
                print("\nYou lost your " + wrong[guess_count].limb + ".\nOnly " + str(
                    total_guess - guess_count) + " body parts left.")
            elif guess_count == (total_guess - 1):
                print("\nYou lost your " + wrong[guess_count].limb + ".\nOnly " + str(
                    total_guess - guess_count) + " body part left.")
    if guess_count == total_guess:
        print("Out of turns, poor Hangman :(\nGame over, thanks for playing.")
    elif guess_count != total_guess and guess_word != secret_word:
        return guess_word
    else:
        print("you win")

hangman()