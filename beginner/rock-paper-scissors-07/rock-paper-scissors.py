#rock paper scissors game day 07
import random

def guess(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

while True:
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = guess(player_choice, computer_choice)
    print(result)
    if input("Do you want to play again? (yes/no): ").lower() != "yes":
        break