import requests
import json


def req(this):
    url = "http://www.floatrates.com/daily/" + str(this['currency_type_for_inverse']) + ".json"
    r = requests.get(url)
    data = json.loads(r.text)
    this['exchange_rates'] = data[this['my_currency_type']]['inverseRate']
    return this


if __name__ == '__main__':
    money = {
        'my_money': int(input("How much money do you want to put into the account?\n")),
        'my_currency_type': input("Currency type what you have:"),
        'currency_type_for_inverse': None,
        'exchange_rates': 0
    }
    all_money = {
        money['my_currency_type']: money['my_money']
    }

    while True:
        if money['my_money'] == 0:
            print('Sorry, You haven`t money on your account!')
            break
        value_money = int(input("Print how much money you what to inverse:"))
        if money['my_money'] - value_money < 0:
            print('Sorry, You can`t inverse this value of money!')
            continue
        type_money = input("Print type of currency what you want:")
        if type_money == money['currency_type_for_inverse']:
            new_money = money['exchange_rates'] * value_money
            money['my_money'] -= value_money
            money[type_money] += new_money
            all_money[money['my_currency_type']] -= value_money
            all_money[type_money] += new_money
        else:
            money['currency_type_for_inverse'] = type_money
            money = req(money)
            new_money = money['exchange_rates'] * value_money
            try:
                money[type_money] += new_money
                all_money[type_money] += new_money
            except KeyError:
                money[type_money] = new_money
                all_money[type_money] = new_money
            money['my_money'] -= value_money
            all_money[money['my_currency_type']] -= value_money
        print('\nAfter inverse you have:')
        print(all_money)
        print('')
        turn = input('You should to continue? (y/n)\n')
        if turn.lower() == 'n' or turn.lower() == 'no':
            break
    print('The final result of the inverse:')
    print(all_money)
