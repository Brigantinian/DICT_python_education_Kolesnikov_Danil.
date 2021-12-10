from random import choice

print("Welcome To Rock-Paper-Scissors")
while True:
    player = input("Select any option\nrock\npaper\nscissors\nexit ").strip().lower()
    computer = choice("rps")
    if player == computer:
        print("Draw")
        print("Computer's choice -> ", computer)
    elif player == "r" and computer == "s" or player == "p" and computer == "r" or player == "s" and computer == "p":
        print("Player Wins")
        print("Sorry, but the computer chose another option and failed:", computer)
    else:
        print("Enter another word")
        print("Sorry, but the computer chose another option:", computer)
    if player == "exit":
     break