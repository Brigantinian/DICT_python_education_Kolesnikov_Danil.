import random


friends = int(input("Enter the number of friends joining (including you):"))


if friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    name = [input() for i in range(friends)]
    new_dict = {name[x - 1]: 0 for x in range(friends + 1)}
    summa = int(input("Enter the total amount: "))
    new_dict_keys = list(new_dict.keys())
    new_dict_keys.sort()


    while True:
        otvet = input('Do you want to use the "Who is lucky?" feature? Write y/n:')
        if otvet == 'y':
            list_amount = [round((summa / (friends - 1)), 2)] * friends
            lucky_friend_index = random.choice(range(friends))
            for i in range(len(new_dict_keys)):
                new_dict[new_dict_keys[i]] = list_amount[i]
            new_dict[new_dict_keys[lucky_friend_index]] = 0
            print(f"{new_dict_keys[lucky_friend_index]} is the lucky one!")
            print(new_dict)
            break
        elif otvet == "n":
            list_amount = [round((summa / friends), 2)] * friends
            for i in range(len(new_dict_keys)):
                new_dict[new_dict_keys[i]] = list_amount[i]
            print("No one is going to be lucky.")
            print(new_dict_keys)
            break
        else:
            print("Incorrect choice. Try again!")
