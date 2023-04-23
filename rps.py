# Rock beats Scissors;
# Scissors beats Paper;
# Paper beats Rock.

import random


player_choice = input("Pick one among Rock, Paper or Scissors: ")
print("Player has picked: " + player_choice)


computer_choices = ["Rock", "Paper", "Scissors"]
computer_pick = random.randrange(0, 3)
computer_choice = computer_choices[computer_pick]
print("Computer has picked: " + computer_choice)

outcome = "Thinking!"

if player_choice == computer_choice:
    outcome = "Tie! Try again!"
    
elif player_choice == "Rock":
    if computer_choice == "Paper":
        outcome = "Computer wins!"
    elif computer_choice == "Scissors":
        outcome = "Player wins!"
        
elif player_choice == "Paper":
    if computer_choice == "Scissors":
        outcome = "Computer wins!"
    elif computer_choice == "Rock":
        outcome = "Player wins!"
        
elif player_choice == "Scissors":        
    if computer_choice == "Rock":
        outcome = "Computer wins!"
    elif computer_choice == "Paper":
        outcome = "Player wins!"
        
else:
    print("Not a valid option. Try again!")

print("Result: " + outcome)