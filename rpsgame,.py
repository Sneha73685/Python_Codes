# rock paper scissors game
import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("Enter a choice (rock, paper, scissors): ").lower()

if player == computer:
    print("computer: ", computer)
    print("player: ", player)
    print("Tie!")

elif player == "rock":
    if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("Paper covers rock, you lose!")
    if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("Rock smashes scissors, you win!")

elif player == "paper":
    if computer == "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("Paper covers rock, you win!")
    if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("Scissors cut paper, you lose!")

elif player == "scissors":
    if computer == "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("PRock smashes scissors, you lose!")
    if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("Scissors cut paper, you win!")