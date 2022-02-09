import random
from operator import add, sub, mul


score = 0
number = 0


while score <= 5:
    action = (add, sub, mul)
    move = random.choice(action)
    x = random.randint(2, 9)
    y = random.randint(2, 9)

    if move == add:
        try:
            print("Example: (", x, "+", y, ")")
            example = int(input())
            answer = move(x, y)
            if example == answer:
                print("Right!")
                score = score + 1
                number = number + 1
            else:
                print("Wrong!")
                number = number + 1
        except:
            print("Incorrect format")

    elif move == sub:
        try:
            print("Example: (", x, "-", y, ") ")
            example = int(input())
            answer = move(x, y)
            if example == answer:
                print("Right!")
                score = score + 1
                number = number + 1
            else:
                print("Wrong!")
                number = number + 1
        except:
            print("Incorrect format")

    elif move == mul:
        try:
            print("Example: (", x, "*", y, ") ")
            example = int(input())
            answer = move(x, y)
            if example == answer:
                print("Right!")
                score = score + 1
                number = number + 1
            else:
                print("Wrong!")
                number = number + 1
        except:
            print("Incorrect format")

    if number == 5:
        print("Your score " + str(score) + "/ 5 .")
        break
