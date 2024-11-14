############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def draw_cards(amount): 
  hand = random.choices(cards, k=amount)
  return hand

def draw_again():
  print("")
  player_choice = input("Type 'y' to get another card, type 'n' to pass: ")
  print("")
  draw_again = True
  if player_choice.lower() == 'y':
    draw_again = True
  elif player_choice.lower() == 'n':
    draw_again = False

  return draw_again



def show_scoreboard(player_cards, computer_cards):
    sum_player_cards = sum(player_cards)
    print(f"  Your cards: {player_cards}, current score: {sum_player_cards}")

    computer_first_card = computer_cards[0]
    print(f"  Computer's first card: {computer_first_card}")  

def determine_winner(player_cards, computer_cards):
  player_final_score = sum(player_cards)
  computer_final_score = sum(computer_cards)
  
  print(f"  Your final hand: {player_cards}, final score: {player_final_score}")
  if player_final_score > 21:
    computer_cards_initial = []
    for card in range(2):
      computer_cards_initial.append(computer_cards[card])
        
    print(f"  Computer's final hand: {computer_cards_initial}, final score: {sum(computer_cards_initial)}")
    print("You went over. You lose 😭")
    return
    
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_final_score}")
  
  if computer_final_score > 21:   
    print("Opponent went over. You win 😁")
    return
    
  if player_final_score > computer_final_score:   
    print("You win 😁")
  elif computer_final_score > player_final_score:
    print("You lose 😭")
  else:
    print("It's a draw 🤝")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(logo)

def determine_ace(card_list):
  if sum(card_list) + 11 > 21:
    return 1
  else:
    return 11

 
def blackjack():
  
  player_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

  if player_choice.lower() == 'y':
    clear()
    player_cards = draw_cards(2)

    computer_cards = draw_cards(2)
    if sum(player_cards) == 22:
      player_cards[1] = 1
    
    if sum(computer_cards) == 22:
      computer_cards[1] = 1
    
    show_scoreboard(player_cards, computer_cards)
   
    while sum(computer_cards) < 17:
      computer_drawn_card = draw_cards(1)
      if computer_drawn_card[0] == 11:
        computer_drawn_card[0] = determine_ace(computer_cards)

      computer_cards.extend(computer_drawn_card)

    add_card = True
    
    while add_card:
      should_draw = draw_again()
      if should_draw: 
        player_drawn_card = draw_cards(1)     
       
        if player_drawn_card[0] == 11:
          player_drawn_card[0] = determine_ace(player_cards)
        
        player_cards.extend(player_drawn_card)

        if sum(player_cards) > 21:
          add_card = False
          determine_winner(player_cards, computer_cards) 
          blackjack()
        else:
          show_scoreboard(player_cards, computer_cards)
      else:
        add_card = False
        determine_winner(player_cards, computer_cards) 
        blackjack()
        
print(logo)
blackjack()        


