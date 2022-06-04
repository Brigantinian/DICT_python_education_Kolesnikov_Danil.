from datetime import date
class Person:

    def __init__(self, name, surname, gender, age, year, month, day):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.year = year
        self.month = month
        self.day = day


    def fio(self):
        print(self.name + ' ' + self.surname + ' ' + self.gender)

    def birthday(self):
        today = date.today()
        one_or_zero = ((today.month, today.day) < (self.month, self.day))
        year_difference = today.year - self.year
        age = year_difference - one_or_zero
        return age

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


vacancy1 = Person("Micle", "Jordan", 'male', 31, 1990, 12, 12)
vacancy2 = Person("Allen", "Iverson", 'male', 20, 2001, 12, 12)
vacancy3 = Person("Glen", "Stasy", 'female', 22, 2000, 3, 3)
vacancy4 = Person("Ann", "Jordan", 'female', 52, 1970, 3, 3)
vacancy5 = Person("Lisa", "Jordan", 'female', 17, 2005, 3, 3)

print(vacancy1.fio())
print(vacancy1.birthday())
print(vacancy1.your_age())
print(vacancy2.fio())
print(vacancy2.birthday())
print(vacancy2.your_age())
print(vacancy3.fio())
print(vacancy3.birthday())
print(vacancy3.your_age())
print(vacancy4.fio())
print(vacancy4.birthday())
print(vacancy4.your_age())
print(vacancy5.fio())
print(vacancy5.birthday())
print(vacancy5.your_age())