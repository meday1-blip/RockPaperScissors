import random

name = input("Your name: ")
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
command = ""

print("Type rock, paper, scissors, or quit.")
while command != "quit":
    command = input("Your move: ").lower()

    if command in choices:
        computer = random.choice(choices)
        print("Computer chose", computer)

        if command == computer:
            print("Tie!")
        elif (command == "rock" and computer == "scissors") or (command == "paper" and computer == "rock") or (command == "scissors" and computer == "paper"):
            player_score += 1
            print(name, "wins!")
        else:
            computer_score += 1
            print("Computer wins!")

        print("Score:", name, player_score, "-", computer_score, "Computer")
    elif command != "quit":
        print("Enter rock, paper, scissors, or quit.")

print("Final score:", name, player_score, "-", computer_score, "Computer")
