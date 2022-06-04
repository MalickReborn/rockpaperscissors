import random
from itertools import combinations_with_replacement


while True:
#Take User Input
     player_action = input("Enter a choice (rock, paper, scissors): ")

#Make the Computer Choose
     possible_actions = ["rock", "paper", "scissors"]
     computer_action = random.choice(possible_actions) 
#computer_action = combinations_with_replacement(possible_actions,1) // another possible input for computer choice
     print(f"\nYou chose {player_action}, computer chose {computer_action}.\n")
#Get a Winner
     if player_action == computer_action:
        print(f"Both players selected {player_action}. It's a tie! No winner!")
     elif player_action == "rock":
         if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
         else:
            print("Paper covers rock! You lose.")
     elif player_action == "paper":
         if computer_action == "rock":
            print("Paper covers rock! You win!")
         else:
            print("Scissors cuts paper! You lose.")
     elif player_action == "scissors":
         if computer_action == "paper":
            print("Scissors cuts paper! You win!")
         else:
            print("Rock smashes scissors! You lose.")
     else:
         print("Not supported")
     play_again = input("Play again? (Yes/No): ")
     if play_again.title() != "Yes":
        break