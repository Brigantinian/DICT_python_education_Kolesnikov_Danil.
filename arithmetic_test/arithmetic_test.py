import random
from operator import add, sub, mul, pow

def _f(xf, yf, move_f, sc, num, s):
    try:
        print("Example: (", xf, s, yf, ")")
        example = int(input())
        answer = move_f(xf, yf)
        if example == answer:
            print("Right!")
            return sc + 1, num + 1
        else:
            print("Wrong!")
            return sc, num + 1
    except:
        print("Incorrect format")


def _save(n, i_f, typ, sc):
    f = open('results.txt', 'a')
    f.write(n)
    f.write(" ,your score (")
    f.write(str(i_f))
    f.write(typ)
    f.write("Result: ")
    f.write(str(sc))
    f.write("\n")
    f.close()


def _result(n, i_f, typ, sc):
    print(n + " ,your score (" + str(i_f) + typ + str(sc) + "/ 5 .")
    turn1 = input("Do you want to save the result?:yes or no"
                  "\nYour answer:")
    if turn1.lower() == "yes":
        _save(n, i, typ, sc)
    turn3 = input("Do you wonna try harder lvl ? yes or no "
                  "\nYour answer:")
    if turn3.lower() == "yes":
        return 0, 0, i + 1
    if turn3.lower() == "no":
        return 6, 6, i


if __name__ == "__main__":
    name = input("What is your name? ")
    print("Hello, " + name + ".")

    turn = input("Turn your lvl : 1 - add,sub,mul(easy,5 exersise)"
                 "                2 - pow (harder,than 1st lvl,10 exersise) "
                 "\nYour answer:")
    score = 0
    number = 0
    i = 1

    if turn == "1":
        while score <= 5:
            action = (add, sub, mul)
            move = random.choice(action)
            x = random.randint(2, (i - 1) * 100 + 9)
            y = random.randint(2, (i - 1) * 100 + 9)
            if move == add:
                score, number = _f(x, y, move, score, number, "+")
            elif move == sub:
                score, number = _f(x, y, move, score, number, "-")
            elif move == mul:
                score, number = _f(x, y, move, score, number, "*")
            if number == 5:
                score, number, i = _result(name, i, " lvl -add, sub, mul)  ", score)

    if turn == "2":
        while score <= 5:
            action1 = (pow,)
            move = random.choice(action1)
            a = random.randint(11, (i - 1) * 100 + 29)
            b = random.randint(0, 3)
            if move == pow:
                score, number = _f(a, b, move, score, number, "**")
            if number == 5:
                score, number, i = _result(name, i, " lvl - pow)  ", score)
