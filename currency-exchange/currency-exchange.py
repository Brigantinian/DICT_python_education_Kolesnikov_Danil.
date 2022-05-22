import requests
import json

a = input("What currency do you want to know in USD and EUR?:\n")
url = "http://www.floatrates.com/daily/"+a+".json"
r = requests.get(url)
data = json.loads(r.text)
exchange_rates = data['usd']
exchange_rates1 = data['eur']

for item in exchange_rates:
    print("{}, {}, {}".format(item, exchange_rates[item],exchange_rates1[item]))