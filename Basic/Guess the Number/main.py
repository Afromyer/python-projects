#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random


def guess_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    random_number = random.randint(1, 101)
    # print(f"Pssst, the correct answer is {random_number}")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty.lower() == 'easy':
        guess_amount = 10
    elif difficulty.lower() == 'hard':
        guess_amount = 5
    else:
        guess_amount = 5

    game_over = False

    def check_guess(guess):
        if guess > random_number:
            print("Too high.")
            return 2
        elif guess < random_number:
            print("Too low.")
            return 1
        else:
            print(f"You got it! The answer was {random_number}")
            return 0

    while game_over == False:
        print(
            f"You have {guess_amount} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        guess_code = check_guess(guess)

        if guess_code > 0:
            guess_amount -= 1
        else:
            game_over = True

        if guess_amount == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was {random_number}")
            game_over = True

    if input("Do you want to play another game? 'y' or 'n': ").lower() == 'y':
        guess_game()


guess_game()
