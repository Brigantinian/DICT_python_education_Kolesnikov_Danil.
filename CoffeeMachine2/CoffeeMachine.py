def buy_coffee(water, milk, beans, cups,money ):
    coffee = input('What do you want to buy? a - espresso, b - latte, c - cappuccino: ')


# water = int(cups) * 200
# milk = int(cups) * 50
# beans = int(cups) * 15
# print("For " + cups + " cups of coffee you will need: ")
# print(str(water) + " ml of water")
# print(str(milk) + " ml of milk")
# print(str(beans) + " g of beans")
water_in_machine = int(input("Write how many ml of water the coffee machine has:"))
# water_in_machine = water // 200
milk_in_machine = int(input("Write how many ml of milk the coffee machine has:"))
# milk_in_machine = milk // 50
beans_in_machine = int(input("Write how many ml of beans the coffee machine has:"))
# beans_in_machine = beans // 15
free_cups = int(input("Write how many cups of coffee the coffee machine has: "))

# ingredients = (beans,water,milk)
# #all_ingredients = all(ingredients)
# min_ingredients = min(ingredients)

cups = int(input("Write how many cups of coffee you will need: "))
max_cups = min(water_in_machine // 200, milk_in_machine // 50,beans_in_machine // 15, free_cups // 1)

# if free_cups == min(ingredients):
#     print("Yes, I can make that amount of coffee")
# elif free_cups > min_ingredients:
#     print("No, I can make only " + str(int(min_ingredients)) + " cups of coffee")
# elif free_cups < min_ingredients:
#     print("Yes, I can make that amount of coffee (and even  " + str(int(min_ingredients - free_cups)) + " more than that)")
print(cups)
print(max_cups)

if max_cups > cups:
    print("Yes, I can make that amount of coffee (and even " + str(max_cups - cups) + " more than that)")
elif cups > max_cups:
    print("No, I can make only " + str(max_cups) + " cups of coffee")
else:
    print("Yes, I can make that amount of coffee")


print("Skolko est v mashiny")
money_in_Machine = 550
water_in_Machine = 400
milk_in_Machine = 540
beans_in_Machine = 120
cups_in_Machine = 9


def ingredients_in_Machine():
    print("The coffee machine has:")
    print(str(water_in_Machine) + " ml of water")
    print(str(milk_in_Machine) + " ml of milk")
    print(str(beans_in_Machine) + " g of coffee beans")
    print(str(cups_in_Machine) + " of free cups")
    print(str(money_in_Machine) + " of grn")


ingredients_in_Machine()



def espresso():
    global money_in_Machine, water_in_Machine, milk_in_Machine, beans_in_Machine, cups_in_Machine
    money_in_Machine += 4
    water_in_Machine -= 250
    beans_in_Machine -= 16
    cups_in_Machine -= 1
    return


def latte():
    global money_in_Machine, water_in_Machine, milk_in_Machine, beans_in_Machine, cups_in_Machine
    money_in_Machine += 7
    water_in_Machine -= 350
    milk_in_Machine -= 75
    beans_in_Machine -= 20
    cups_in_Machine -= 1


def cappuccino():
    global money_in_Machine, water_in_Machine, milk_in_Machine, beans_in_Machine, cups_in_Machine
    money_in_Machine += 6
    water_in_Machine -= 200
    milk_in_Machine -= 100
    beans_in_Machine -= 12
    cups_in_Machine -= 1

    while True:
        print("Write action, what you what to choose (buy, fill, take)")
        answer = input()
        if answer == "buy":
            while True:
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino")
                x = input()
                if x == "1":
                    espresso()
                    ingredients_in_Machine()
                    break
                elif x == "2":
                    latte()
                    ingredients_in_Machine()
                    break
                elif x == "3":
                    cappuccino()
                    ingredients_in_Machine()
                    break
                else:
                    print("Please, answer what kind of coffe , do you want buy")
        elif answer == "take":
            print("I gave you " + str(money_in_Machine))
            money_in_Machine *= 0
            ingredients_in_Machine()
        elif answer == "fill":
            new_water = int(input("Write how many ml of watter you want add: "))
            new_milk = int(input("Write how many ml of milk you want add: "))
            new_beans = int(input("Write how many grams of coffee beans you want add: "))
            new_cups = int(input("Write how many disposable cups you want add: "))


            water_in_Machine += new_water
            milk_in_Machine += new_milk
            beans_in_Machine += new_beans
            cups_in_Machine += new_cups


            ingredients_in_Machine()


            break


if water_in_Machine < 0 :
        print("Sorry, not enough water")
        money_in_Machine -= 4
        water_in_Machine += 250
        beans_in_Machine += 16
        cups_in_Machine += 1
    elif beans_in_Machine < 0 :
        print("Sorry, not enough coffee beans")
        money_in_Machine -= 4
        water_in_Machine += 250
        beans_in_Machine += 16
        cups_in_Machine += 1
    elif cups_in_Machine < 0 :
        print("Sorry, not enough cups")
        money_in_Machine -= 4
        water_in_Machine += 250
        beans_in_Machine += 16
        cups_in_Machine += 1


