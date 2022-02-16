import random
from operator import add, sub, mul, pow

name = input("What is your name? ")
print("Hello, " + name + ".")

turn = input("Turn your lvl : 1 - add,sub,mul(easy,5 exersise)"
             "                2 - pow (harder,than 1st lvl,10 exersise) "
             "\nYour answer:")

score = 0
number = 0

if turn == "1":
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
            print(name+" ,your score (1 lvl -add, sub, mul)  " + str(score) + "/ 5 .")

            turn1 = input("Do you want to save the result?:yes or no"
                          "\nYour answer:")
            if turn1 == "yes":
                f = open('results.txt', 'w')
                f.write(name)
                f.write(" ,your score (1 lvl -add, sub, mul)  ")
                f.write("Result: ")
                f.write(str(score))
                f.write("\n")
                f.close()
                break
            if turn1 == "no":
                break

if turn == "2":
    while score <= 5:
        action1 = (pow,)
        move = random.choice(action1)
        a = random.randint(11, 29)
        b = random.randint(11, 29)

        if move == pow:
            try:
                print("Example: (", a, "**", b, ") ")
                example = int(input())
                answer = move(a, b)
                if example == answer:
                    print("Right!")
                    score = score + 1
                    number = number + 1
                else:
                    print("Wrong!")
                    number = number + 1
            except:
                print("Incorrect format")

        if number == 10:
            print(name+" ,your score (2 lvl - pow) " + str(score) + "/ 10 .")

            turn1 = input("Do you want to save the result?:yes or no"
                          "\nYour answer:")
            if turn1 == "yes":
                f = open('results.txt', 'w')
                f.write(name)
                f.write(" ,your score (2 lvl - pow) ")
                f.write("Result: ")
                f.write(str(score))
                f.write("\n")
                f.close()
                break
            if turn1 == "no":
                break
