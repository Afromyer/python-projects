import random
from game_data import data
import art
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_questions(comparison_list):
    name1 = comparison_list[0]["name"]
    description1 = comparison_list[0]["description"]
    country1 = comparison_list[0]["country"]

    name2 = comparison_list[1]["name"]
    description2 = comparison_list[1]["description"]
    country2 = comparison_list[1]["country"]

    print(f"Compare A: {name1}, a {description1}, from {country1}.")
    print(art.vs)
    print(f"Against B: {name2}, a {description2}, from {country2}.")


def compare_questions(comparison_list):
    follower_count1 = comparison_list[0]["follower_count"]
    follower_count2 = comparison_list[1]["follower_count"]

    more_followers = ""

    if follower_count1 > follower_count2:
        more_followers = "A"
        #print("Pssst, 'A' has more followers :)")
    elif follower_count1 < follower_count2:
        more_followers = "B"
        #print("Pssst, 'B' has more followers :)")

    user_answer = input("Who has more followers? Type 'A' or 'B': ")

    if user_answer.upper() == more_followers.upper():
        return True
    else:
        return False


def higher_or_lower():
    game_over = False
    score = 0
    while game_over == False:
        print(art.logo)
        comparisons = random.choices(data, k=2)

        if comparisons[0] == comparisons[1]:
            comparisons[1] = random.choice(data)

        if score > 0:
            print(f"You're right! Current score: {score}.")

        generate_questions(comparisons)
        result = compare_questions(comparisons)

        if result == True:
            score += 1
            clear_console()
        else:
            clear_console()
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

            new_game = input("Do you want to play again? Type 'y' or 'n': ")

            if new_game.lower() == 'y':
                higher_or_lower()


higher_or_lower()
