import random
from operator import add, sub, mul

score = 0
while score <= 9:
    action = (add, sub, mul)
    move = random.choice(action)
    x = random.randint(2,9)
    y = random.randint(2,9)

    if move == add:
        print("", x, "add",y, "")
        example = int(input())
        answer = move(x,y)
        if example == answer:
            print("Right!")

        else:
            print("Wrong!")

    elif move == sub:
        print("", x, "sub", y, " ")
        example = int(input())
        answer = move(x,y)
        if example == answer:
            print("Right!")
        else:
            print("Wrong!")

    elif move == mul:
        print("", x, "mul", y, " ")
        example = int(input())
        answer = move(x,y)
        if example == answer:
            print("Right!")
        else:
            print("Wrong!")
