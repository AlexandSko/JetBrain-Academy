import random
import string


def menu():
    print("H A N G M A N")
    while True:
        command = input('Type "play" to play the game, "exit" to quit: ')
        if command not in ["play", 'exit']:
            continue
        return command == "play"


while menu():

    words = ['python', 'java', 'kotlin', 'javascript']

    answer = list(random.choice(words))
    answer_set = set(answer)

    opened_letters = list("-" * len(answer))
    guessed_letters = set(opened_letters)

    entered_letters = set()

    lives = 8

    while lives != 0:
        # Print game field and wait for player input
        print("\n", "".join(opened_letters))
        letter = input(f"Input a letter: ")

        # Check if the player input is correct
        exceptions = [letter in entered_letters,
                      letter not in string.ascii_lowercase,
                      len(letter) != 1]

        if exceptions[0]:
            print("You already typed this letter")
        else:
            entered_letters.add(letter)

        if exceptions[1]:
            print("It is not an ASCII lowercase letter")

        if exceptions[2]:
            print("You should input a single letter")

        if any(exceptions):
            continue

        # Check either the player guessed a letter or not
        if letter in answer_set:

            # Find all indexes of the inputted letter in the answer(hidden word)
            for ind, elem in enumerate(answer):
                if elem == letter:

                    opened_letters[ind] = letter  # Open the guessed letter to the player

            answer_set.discard(letter)
            guessed_letters.add(letter)

        else:
            lives -= 1
            print("No such letter in the word")

        # Print the result of the game (The player won)
        if opened_letters == answer:
            print("You guessed_letters the word!", "You survived!\n", sep='\n')
            break
    # Print the result of the game (The player lost)
    else:
        print("You are hanged!\n")
