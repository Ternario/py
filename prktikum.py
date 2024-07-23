from datetime import datetime
from dateutil.relativedelta import relativedelta

# --------------------------------------task 1---------------------------------------------

cars = [
    ("Bobic obiknovenniy", 2024, "Red"),
    ("Honda Accord ", 2019, "Blue"),
    ("Ford Mustang GT", 2001, "Black"),
    ("Chevrolet 23 ", 2008, "Yellow"),
    ("Tesla 1 ", 2002, "White"),
    ("BMW 3", 2021, "Blue"),
    ("Audi A4", 2010, "Black"),
    ("Mercedes-Benz C", 2019, "Silver"),
    ("Hyundai 45", 2012, "Red"),
    ("Volkswagen Golf plus", 2006, "Green")
]


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.model}, {self.year}, {self.color}"

    def __repr__(self):
        return f"{self.model}, {self.year}, {self.color}"


my_objects = [Car(i, y, z) for i, y, z in cars]

filter_object = filter(lambda x: x.color == "Black", my_objects)

# --------------------------------------task 2---------------------------------------------

persons = [
    ("Анна", "1990-05-15"),
    ("Иван", "1985-07-20"),
    ("Ольга", "2020-10-30"),
    ("Сергей", "1992-03-25"),
    ("Елена", "1988-06-05"),
    ("Алексей", "1975-12-12"),
    ("Мария", "1993-08-22"),
    ("Дмитрий", "2008-11-01"),
    ("Наталья", "2015-04-15"),
    ("Владимир", "1995-09-09")
]


def is_valid_age(birthdate: str):
    year, month, day = map(int, birthdate.split('-'))
    date_of_birth = datetime(year, month, day)
    now = datetime.now()
    age = relativedelta(now, date_of_birth).years
    return age


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __str__(self):
        return f"{self.name}, {self.birthday}"

    def __repr__(self):
        return f"{self.name}, {self.birthday}"

    def calk_age(self):
        return is_valid_age(self.birthday)


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

    def __repr__(self):
        return f"{self.name}, {self.age}"

    def is_adult(self):
        return self.age > 18


list_of_person = [Person(i, y) for i, y in persons]

list_of_employee = filter(lambda x: x.is_adult(), [Employee(i.name, i.calk_age()) for i in list_of_person])

print(all(i.age > 18 for i in list_of_employee))
