print("аргентинское песо - 1 mycoin = 0.82 ARS;\n"
        "гондурасская лемпира - 1 mycoin = 0.17 HNL;\n"
        "австралийский доллар - 1 mycoin = 1.9622 AUD;\n"
        "марокканский дирхам - 1 mycoin = 0.208 MAD.\n"
        "американский доллар - 1 mycoin = 3.21 USD")


print("Please, enter the number of mycoins you have:")
a = float(input())
print("Please, enter the exchange rate:")
# b = float(input())
k = float(a * 0.82)
q = float(a * 0.17)
s = float(a * 1.9622)
d = float(a * 0.208)
f = float(a * 3.21)
print("I will get "+ str(k) +" ARS from the sale of "+ str(a) +" mycoins.")
print("I will get "+ str(q) +" HNL from the sale of "+ str(a) +" mycoins.")
print("I will get "+ str(s) +" AUD from the sale of "+ str(a) +" mycoins.")
print("I will get "+ str(d) +" MAD from the sale of "+ str(a) +" mycoins.")
print("I will get "+ str(f) +" USD from the sale of "+ str(a) +" mycoins.")