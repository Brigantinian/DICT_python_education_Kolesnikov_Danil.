import random
import names
from datetime import date


class Person:
    def __init__(self, name, surname, gender, age, birthday):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.birthday = birthday

    def fio(self):
        print(self.name + ' ' + self.surname + ' ' + self.gender)

    def your_age(self):
        if self.gender == "male":
            if self.age >= 18 and self.age <= 25:
                print('Your vacancy is courier!')
            elif self.age >= 25:
                print('Your vacancy is engineer!')
            else:
                print('There are currently no vacancies for you')
        if self.gender == "female":
            if self.age >= 20 and self.age <= 30:
                print('Your vacancy is secretary!')
            elif self.age >= 45:
                print('Your vacancy is cleaner!')
            else:
                print('There are currently no vacancies for you')

    def __repr__(self) -> str:
        return f'Person({self.name} {self.surname},{self.gender},{self.age})'


class Generator:
    genders = ['male', 'female']
    vacancies = ['courier', 'engeneer', 'secretary', 'cleaner']

    def __date(self) -> str:
        genders = ['male', 'female']
        vacancies = ['courier', 'engeneer', 'secretary', 'cleaner']
        y = date.today().year
        year = random.randint(1920, date.today().year)
        month = random.randint(1, 12)
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        elif month == 2:
            day = random.randint(1, 28)
        else:
            day = random.randint(1, 30)
        y1 = y - year

        if genders == 'male':
            y1 = y - year
            if y1 >= 18 and y1 <= 25:
                d = ('Your vacancy is courier!')
                print(d)
            elif y1 >= 25:
                d = ('Your vacancy is engineer!')
                print(d)
            else:
                d = ('There are currently no vacancies for you')
                print(d)
            return d
        if genders == "female":
            y1 = y - year
            if y1 >= 20 and y1 <= 30:
                d1 = ('secretary!')
                print(d1)
            elif y1 >= 45:
                d1 = ('cleaner!')
                print(d1)
            else:
                d1 = (' no vacancies ')
                print(d1)
                return d1
        return ('born: {:04d}-{:02d}-{:02d},{:02d} years old'.format(year, month, day, y1))

    def generate_one(self) -> Person:
        gen = random.randint(0, 1)
        gender = self.genders[gen]
        name = names.get_first_name(gender)
        surname = names.get_last_name()
        birthday = self.__date()
        work = self.__date()
        return Person(name, surname, gender, birthday, work)

    def generate_1000(self) -> list:
        plist = list()
        for i in range(1000):
            plist.append(self.generate_one())
        return plist

    def generate_10000(self) -> Person:
        plist1 = list()
        for i in range(10000):
            plist1.append(self.generate_one())
        return plist1


if __name__ == '__main__':
    g = Generator()
    print(g.generate_1000())
    print(g.generate_10000())
