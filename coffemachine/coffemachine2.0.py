print("How many cups you need ?:")
cups = input()
print('For ' + str(cups) + ' cups of coffee you will need:')
water = cups * 200
milk = cups * 50
beans = cups * 15
print(str(water) + ' ml of water')
print(str(milk) + ' ml of milk')
print(str(beans) + ' ml of coffee beans')

print("""
1-Starting to make a coffee
2-Grinding coffee beans
3-Boiling water
4-Mixing boiled water with crushed coffee beans
5-Pouring coffee into the cup
6-Pouring some milk into the cup
7-Coffee is ready!""")

print('Write how many ml of water the coffee machine has:')
water = int(input())
print('Write how many ml of milk the coffee machine has:')
milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
beans = int(input())
print('Write how many cups coffee you need ? :')
cups = int(input())
Cups = water // 200 or milk // 50 or beans // 15

if cups > Cups:
    print('No, I can make only ' + str(Cups) + ' cups of coffee.')
elif cups == Cups:
    print('Yes, I can make that amount of coffee.')
else:
    newCups = Cups - cups
    print('Yes, I can make that amount of coffee (and even ' + str(newCups) + ' more than that)')
