def take_coffee(water, milk, coffee_beans, cups):
    coffee = input('Starting to make a coffee? a - espresso, b - cappuccino, c - latte: ')
    coffee_espresso_water = 200
    coffee_espresso_milk = 50
    coffee_espresso_coffee_beans = 15
    if coffee == '1':
        water -= coffee_espresso_water
        milk -= coffee_espresso_milk
        coffee_beans -= coffee_espresso_coffee_beans
        cups -= 1
        print("Write how many cups of coffee you will need:")
        print('The coffee machine has:')
        water = 5000
        milk = 1250
        coffee_beans = 375