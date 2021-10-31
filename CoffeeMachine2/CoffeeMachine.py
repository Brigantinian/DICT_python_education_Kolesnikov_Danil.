class Coffee_Machine() :
    def __init__(self):
        self.money_in_Machine = 550
        self.water_in_Machine = 400
        self.milk_in_Machine = 540
        self.beans_in_Machine = 120
        self.cups_in_Machine = 9

    def ing_in(self):
        print("The coffee machine has:")
        print(str(self.water_in_Machine) + " ml of water")
        print(str(self.milk_in_Machine) + " ml of milk")
        print(str(self.beans_in_Machine) + " g of coffee beans")
        print(str(self.cups_in_Machine) + " of disposable cups")
        print(str(self.money_in_Machine) + " of grn")

    def espresso(self):
            self.money_in_Machine += 4
            self.water_in_Machine -= 250
            self.beans_in_Machine -= 16
            self.cups_in_Machine -= 1
            print("I have enough resources, making you a coffee!")
            if self.water_in_Machine < 0:
                print("Sorry, not enough water")
                self.money_in_Machine -= 4
                self.water_in_Machine += 250
                self.beans_in_Machine += 16
                self.cups_in_Machine += 1
            elif self.beans_in_Machine < 0:
                print("Sorry, not enough coffee beans")
                self.money_in_Machine -= 4
                self.water_in_Machine += 250
                self.beans_in_Machine += 16
                self.cups_in_Machine += 1
            elif self.cups_in_Machine < 0:
                print("Sorry, not enough cups")
                self.money_in_Machine -= 4
                self.water_in_Machine += 250
                self.beans_in_Machine += 16
                self.cups_in_Machine += 1
            return

    def latte(self):
            self.money_in_Machine += 7
            self.water_in_Machine -= 350
            self.milk_in_Machine -= 75
            self.beans_in_Machine -= 20
            self.cups_in_Machine -= 1
            print("I have enough resources, making you a coffee!")
            if self.water_in_Machine < 0 :
                print("Sorry, not enough water")
                self.money_in_Machine -= 7
                self.water_in_Machine += 350
                self.milk_in_Machine += 75
                self.beans_in_Machine += 20
                self.cups_in_Machine += 1
            elif self.milk_in_Machine < 0:
                print("Sorry, not enough milk")
                self.money_in_Machine -= 7
                self.water_in_Machine += 350
                self.milk_in_Machine += 75
                self.beans_in_Machine += 20
                self.cups_in_Machine += 1
            elif self.beans_in_Machine < 0:
                print("Sorry, not enough coffee beans")
                self.money_in_Machine -= 7
                self.water_in_Machine += 350
                self.milk_in_Machine += 75
                self.beans_in_Machine += 20
                self.cups_in_Machine += 1
            elif self.cups_in_Machine < 0:
                print("Sorry, not enough cups")
                self.money_in_Machine -= 7
                self.water_in_Machine += 350
                self.milk_in_Machine += 75
                self.beans_in_Machine += 20
                self.cups_in_Machine += 1
            return

    def cappuccino(self):
            print("I have enough resources, making you a coffee!")
            self.money_in_Machine += 6
            self.water_in_Machine -= 200
            self.milk_in_Machine -= 100
            self.beans_in_Machine -= 12
            self.cups_in_Machine -= 1
            if self.water_in_Machine < 0:
                print("Sorry, not enough water")
                self.money_in_Machine -= 6
                self.water_in_Machine += 200
                self.milk_in_Machine += 100
                self.beans_in_Machine += 12
                self.cups_in_Machine += 1
            elif self.milk_in_Machine < 0:
                print("Sorry, not enough milk")
                self.money_in_Machine -= 6
                self.water_in_Machine += 200
                self.milk_in_Machine += 100
                self.beans_in_Machine += 12
                self.cups_in_Machine += 1
            elif self.beans_in_Machine < 0:
                print("Sorry, not enough milk")
                self.money_in_Machine -= 6
                self.water_in_Machine += 200
                self.milk_in_Machine += 100
                self.beans_in_Machine += 12
                self.cups_in_Machine += 1
            elif self.cups_in_Machine < 0:
                print("Sorry, not enough milk")
                self.money_in_Machine -= 6
                self.water_in_Machine += 200
                self.milk_in_Machine += 100
                self.beans_in_Machine += 12
                self.cups_in_Machine += 1
            return


coffee = Coffee_Machine()
while True:
        print("Write action (buy, fill, take, remaining, exit)")
        answer = input()
        if answer == "buy":
            while True:
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - back to  menu:")
                x = input()
                if x == "1":
                    coffee.espresso()
                    break
                elif x == "2":
                    coffee.latte()
                    break
                elif x == "3":
                    coffee.cappuccino()
                    break
                elif x == "4":
                    break
                else:
                    print("Please, answer what do you want buy")
        elif answer == "take":
            print("I gave you " + str(coffee.money_in_Machine))
            coffee.money_in_Machine *= 0
        elif answer == "fill":
            added_water = int(input("Write how many ml of watter you want add: "))
            added_milk = int(input("Write how many ml of milk you want add: "))
            added_beans = int(input("Write how many grams of coffee beans you want add: "))
            added_cups = int(input("Write how many disposable cups you want add: "))

            coffee.water_in_Machine += added_water
            coffee.milk_in_Machine += added_milk
            coffee.beans_in_Machine += added_beans
            coffee.cups_in_Machine += added_cups
        elif answer == "remaining":
            coffee.ing_in()
        elif answer == "exit":
         break


def Coffee_Machine():
    return More_coffee()

def More_coffee ():
    while True:
        again = input("Do you wonna more coffe? Please type y for yes or n for no-")
        if again not in {"y","n"}:
            print("please enter valid input")
        elif again == "n":
            return "Thank you , bye!"
        elif again == "y" :
          return Coffee_Machine()
More_coffee()
