# ингридиентов в кофеварке
money = 550
water = 400
milk = 540
beans = 120
cups = 9

class CustomError(Exception):
    pass

# CustomError(собственный) - пользовательское исключение
# Exception(встроенный) - заканчиваются полностью системные исключения  и начинаются обыкновенные, с которыми можно работать.

# кол-во каждого ингридиента в машине
def print_state():
    print()
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()

# выбор действия
def select_action() -> str:
    print("ATTENCION!!! Here you must write words no numbers!")
    return input('Write action:\n 1-buy\n 2-fill\n 3-take\n 4-remaining\n 5-exit\n:')

# выбор 1 из 3 вариантов кофе
def select_coffe() -> int:
    print()
    move = input('What do you want to buy?'
                 ' 1 - espresso,'
                 ' 2 - latte,'
                 ' 3 - cappuccino,'
                 ' 4 - back to main menu: ')
    if move == '4':
        return 0
    return int(move)

# проверка ,на ,достаточно ли ингр. в машине
def is_enough(need_water=0, need_milk=0, need_beans=0):
    if water < need_water:
        print('Sorry, not enough water!\n')
        raise CustomError
    if milk < need_milk:
        print('Sorry, not enough milk!\n')
        raise CustomError
    if beans < need_beans:
        print('Sorry, not enough beans!\n')
        raise CustomError
    if cups < 1:
        print('Sorry, not enough cups\n')
        raise CustomError
    print('I have enough resources, making you a coffee!\n')

# raise - позволяет вызвать конкретное исключение.

# функция, для покупки кофе
def buy():
    global money, water, milk, beans, cups

    variants = select_coffe()

    try:
        if variants == 0:
            pass
        elif variants == 1:  # espresso
            is_enough(need_water=250, need_beans=16)

            money += 4
            water -= 250
            beans -= 16
            cups -= 1
        elif variants == 2:  # latte
            is_enough(need_water=350, need_milk=75, need_beans=20)

            money += 7
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
        elif variants == 3:  # cappuccino
            is_enough(need_water=200, need_milk=100, need_beans=12)

            money += 6
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
        else:
            raise ValueError(f'Unknown variant {variants}')
    except CustomError:
        pass

# функция,для наполнения кофемашины
def fill():
    global water, milk, beans, cups

    print()
    water += int(input('Write how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    beans += int(input('Write how many grams of coffee beans'
                       ' do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee'
                      ' do you want to add: '))
    print()

#  функция, для изьятия денег из машины
def take():
    global money

    print()
    print(f'I gave you {money} griven')
    print()

    money = 0

def menu():
    while True:
        action = select_action()

        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'exit':
            break
        elif action == 'remaining':
            print_state()
        else:
            raise ValueError(f'Unknown command {action}')

menu()