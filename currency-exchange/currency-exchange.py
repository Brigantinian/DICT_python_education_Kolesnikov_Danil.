import requests
import json

turn = input("MOney :  yes"
             "      or           no "
             "\nYour answer:")
while True:
    if turn == "yes":
        b = input("How much money do you want to put into the account?\n")
        c = input("OK ,on your account :" + b)
        q = input("Currency what you have:")
        n = input("Currency what you want:")
        print(q + " in  " + n)

        url = "http://www.floatrates.com/daily/" + n + ".json"
        url2 = "http://www.floatrates.com/daily/" + q + ".json"
        r = requests.get(url)
        r1 = requests.get(url2)
        data = json.loads(r.text)
        data1 = json.loads(r1.text)
        exchange_rates2 = data[q]['inverseRate']
        print("In your cache")
        print(n)
        dengi = input((exchange_rates2) * int(b))
        while True:
            try:
                turn1 = input("You wonna to continue: yes or no?")
                if turn1 == "yes":
                    print("On your account?\n" + str((exchange_rates2) * int(dengi)))
                    q = input("Currency what you have:"+n)
                    n1 = input("Currency what you want:")
                    print(n + " in  " + n1)
                    url = "http://www.floatrates.com/daily/" + n1 + ".json"
                    url2 = "http://www.floatrates.com/daily/" + n + ".json"
                    r = requests.get(url)
                    r1 = requests.get(url2)
                    data = json.loads(r.text)
                    data1 = json.loads(r1.text)
                    exchange_rates2 = data[n]['inverseRate']
                    print("In your cache")
                    print(n1)
                    print((exchange_rates2) * int(b))
                if turn1 == "no":
                    print("Bye!")
                    break
            except:
                print("Sorry , not enough money ! Bye!")
                break
    break