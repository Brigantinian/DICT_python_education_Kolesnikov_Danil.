from random import choice

print("Welcome To Rock-Paper-Scissors")
player = input("Select any option\nrock\npaper\nscissors ").strip().lower()
computer = choice("rock,paper,scissors")
if player==computer:
    print("Draw")
    print("Computer's choice -> ",computer)
elif player=="r" and computer=="p" or player=="p" and computer=="s" or player=="s" and computer=="r":
    print("Computer's choice -> ",computer)
else:
    print("Enter another word")
    print("Sorry, but the computer chose another option:",computer)