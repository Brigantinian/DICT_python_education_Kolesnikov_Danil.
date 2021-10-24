def buy_coffee(water, milk, coffee_beans, disposable_cups, money):
    coffee = input('What do you want to buy? a - espresso, b - latte, c - cappuccino: ')





caps = input("Write how many cups of coffee you will need: ")
water = int(caps) * 200
milk = int(caps) * 50
beans = int(caps) * 15
print("For " + caps + " cups of coffee you will need: ")
print(str(water) + " ml of water")
print(str(milk) + " ml of milk")
print(str(beans) + " g of beans")
water_in_machine = int(input("Write how many ml of water the coffee machine has:"))
water_in_machine = water // 200
milk_in_machine = int(input("Write how many ml of milk the coffee machine has:"))
milk_in_machine = milk // 50
beans_in_machine = int(input("Write how many ml of beans the coffee machine has:"))
beans_in_machine = beans // 15
free_cups = int(input("Write how many cups of coffee you will need: "))

ingredients = (beans,water,milk)
all_ingredients = all(ingredients)

if free_cups == all_ingredients:
    print("Yes, I can make that amount of coffee")
elif free_cups < all_ingredients:
    print("No, I can make only " + str(all_ingredients) + " cups of coffee")
elif free_cups > all_ingredients:
    print("Yes, I can make that amount of coffee (and even more " + str(int(all_ingredients-free_cups)) + " than that)")



