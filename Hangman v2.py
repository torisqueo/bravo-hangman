# updates:
    # include words with multiples of the same letter
    # accounted for spaces, apostrophies, commas
    # prints a notice if you've already used that letter
    # notice of non-letter entries and repeated letters

import random

word_ops = ["clip", "mention it all", "morgan letters", "i made it nice", "go to sleep",
            "uncool", "cabaret", "summer should be fun", "giggly squad", "more life",
            "send it", "activated", "loverboy", "goodbye kyle", "bravo bravo fucking bravo",
            "morally corrupt faye resnick", "maloof hoof", "prostitution whore", "thick as thieves",
            "it's about tom"]

def hangman():
    # setup
    secret_word = random.choice(word_ops)
    combo = ""
    guess_word = list(str("_") * (len(secret_word)))
#    if " " in secret_word:
    for n, i in enumerate(secret_word):
        if i == " ":
            enumerate(guess_word)
            guess_word[n] = " "
        elif i == ",":
            enumerate(guess_word)
            guess_word[n] = ","
        elif i == "'":
            enumerate(guess_word)
            guess_word[n] = "'"

    combo = ''.join(guess_word)

    # hangman_body():
    limb = ["body", "left arm", "right arm", "left leg", "right leg", "torso", "head"]

    # guessing
    guess_count = 0
    total_guess = (len(limb))
    guess_list = []

    # play on
    print(combo)

    while combo != secret_word and guess_count != total_guess:
        guess = input("\nEnter a letter: ")
        guess = guess.lower()

        if guess in guess_list:
            print("You've already guessed that letter, please guess a new letter.")

        if guess in secret_word:
            for n, i in enumerate(secret_word):
                if i == guess:
                    enumerate(guess_word)
                    guess_word[n] = guess
                    combo = ''.join(guess_word)
            guess_list.append(guess)
            print(combo)

        elif guess not in secret_word and guess not in guess_list:
            alpha = "abcdefghijklmnopqrstuvwxyz"
            if guess not in alpha:
                print("Please enter a letter A-Z")
            else:
                guess_count += 1
                if guess_count < (total_guess - 1):
                    print("\nYou lost your " + limb[guess_count] + ".\nOnly " + str(
                        total_guess - guess_count) + " body parts left.")
                elif guess_count == (total_guess - 1):
                    print("\nOne more wrong guess and you'll lose your " + limb[-1] + "!")
            guess_list.append(guess)


    if combo == secret_word:
        print("Congrats, you correctly guessed the phrase and saved your hangman!")
    elif guess_count == total_guess:
        print("Out of turns, poor Hangman :(\nGame over, thanks for playing.")
    elif guess_count != total_guess and guess_word != secret_word:
        return guess_word

hangman()