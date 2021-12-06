import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--interest')
parser.add_argument('--annuity')
parser.add_argument('--payment')
parser.add_argument('--periods')
arg = parser.parse_args()

type = arg.type
principal = arg.principal
interest = arg.interest
annuity = arg.annuity
payment = arg.payment
periods = arg.periods

print(principal, interest, annuity, periods, payment,type)

def func1(principal ,periods , interest):
        p = int(principal)
        per = int(periods)
        percent = int(interest)
        interest = percent / (12 * 100)
        if percent != 0:
            interest = float(percent)
            i = percent / (12 * 100)
            m = 1
            D = 0
            while m <= per:
                d = (p / per) + (i * (p - (p * (m - 1) / per)))
                print("Month {}: paid out {}".format(m, math.ceil(d)))
                m += 1
                D += math.ceil(d)
                print("Overpayment = {}".format(D - d))
            else:
                print("Incorrect Par3")
        else:
            print("Incorrect Par4")


def func2( principal,  payment , interest,i,x):
        p = int(principal)
        pay1 = int(payment)
        percent = int(interest)
        interest = percent / (12 * 100)
        if percent:
            percent = float(interest)
            i = percent / (12 * 100)
            x = int(pay1) / (int(pay1) - (interest / 1200 * int(p)))
            degree = math.log(int(pay1) / (int(pay1) - (interest / 1200 * int(p))),
                              (1 + interest / 1200))
            year = math.ceil(degree) / 12
            r = str(round(year, (1)))
            print("It will take", list(r)[0], "years and", list(r)[2], "months to repay this loan!")
            print("Overpayment =", p * math.ceil(degree) - int(pay1))
        else:
            print("Incorrect Par8")



def func3(periods, payment,  interest):
        per = int(periods)
        pay2 = int(payment)
        percent = int(interest)
        interest = percent / (12 * 100)
        if percent == interest:
            percent = float(interest)
            i = percent / (12 * 100)
            num = pow(1 + i, int(per))
            a = i * (1 + i) ** int(per)
            b = (1 + i) ** int(per) - 1
            c = i * (1 + i) ** int(per) / (1 + i) ** int(per) - 1
            d = float(pay2) / i * (1 + i) ** int(per) / (1 + i) ** int(per) - 1
            result_p = math.floor(float(float(payment) / ((i * num) / (num - 1))))
            print("Your loan principal =", round(d), "!")
            print('Overpayment =', float(pay2) * int(per) - result_p)
        else:
            print("Incorrect Par12")




# if __name__=="__main__":
#      if principal and periods and interest:
#         p = int(principal)
#         per = int(periods)
#         percent = int(interest)
#         interest = percent / (12 * 100)
#         if percent != 0:
#             interest = float(percent)
#             i = percent / (12 * 100)
#             m = 1
#             D = 0
#             while m <= per:
#                 d = (p / per) + (i * (p - (p * (m - 1) / per)))
#                 print("Month {}: paid out {}".format(m, math.ceil(d)))
#                 m += 1
#                 D += math.ceil(d)
#                 print("Overpayment = {}".format(D - d))
#             else:
#                 print("Incorrect Par3")
#         else:
#             print("Incorrect Par4")
#
# if __name__=="__main__":
#      if principal and payment and interest:
#         p = int(principal)
#         pay1 = int(payment)
#         percent = int(interest)
#         interest = percent / (12 * 100)
#         if percent:
#             percent = float(interest)
#             i = percent / (12 * 100)
#             x = int(pay1) / (int(pay1) - (interest / 1200 * int(p)))
#             degree = math.log(int(pay1) / (int(pay1) - (interest / 1200 * int(p))),
#                                       (1 + interest / 1200))
#             year = math.ceil(degree) / 12
#             r = str(round(year, (1)))
#             print("It will take", list(r)[0], "years and", list(r)[2], "months to repay this loan!")
#             print("Overpayment =", p * math.ceil(degree) - int(pay1))
#         else:
#          print("Incorrect Par8")
#      else:
#       print("Incorrect Par9")
#
# if __name__=="__main__":
#     if periods and payment and interest:
#         per = int(periods)
#         pay2 = int(payment)
#         percent = int(interest)
#         interest = percent / (12 * 100)
#         if percent == interest:
#             percent = float(interest)
#             i = percent / (12 * 100)
#             num = pow(1 + i, int(per))
#             a = i * (1 + i) ** int(per)
#             b = (1 + i) ** int(per) - 1
#             c = i * (1 + i) ** int(per) / (1 + i) ** int(per) - 1
#             d = float(pay2) / i * (1 + i) ** int(per) / (1 + i) ** int(per) - 1
#             result_p = math.floor(float(float(payment) / ((i * num) / (num - 1))))
#             print("Your loan principal =", round(d), "!")
#             print('Overpayment =', float(pay2) * int(per) - result_p)
#         else:
#             print("Incorrect Par12")
#     else:
#         print("Incorrect Par13")
