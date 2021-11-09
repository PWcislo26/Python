from datetime import datetime


# zad1
class Student():

    def __init__(self, name, marks):
        self._name = name
        self._marks = marks

    def is_passed(self):
        if self._marks > 50:
            return True
        return False

    @property
    def name(self):
        return self._name


student1 = Student("Piotr", 57)
print(student1.is_passed())

student2 = Student("Alicja", 36)
print(student2.is_passed())


# zad2
class Library():
    def __init__(self, city, street, zip_code, open_hours, phone):
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self) -> str:
        return f"Library in {self._city} on {self._street}"


class Order():
    def __init__(self, employee, student, books, order_date) -> None:
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date

    def __str__(self) -> str:
        return f"Order is being processed by {self._employee}. Order consists of {self._books}."


class Employee():
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self) -> str:
        return f"Employee {self._first_name} {self._last_name} living in {self._city}"


class Book():
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages) -> None:
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Book written by {self._author_name} {self._author_surname}, currently in {self._library}"


library1 = Library("Katowice", "3_maja", "41-200", "8-16", 602354971)
library2 = Library("Sosnowiec", "XYZ", "42-323", "9-17", 606323953)
book1 = Book(library1, 1964, "Alfred", "XYZ", 543)
book2 = Book(library1, 1999, "Norman", "Nolan", 2211)
book3 = Book(library2, 2005, "Norbert", "Gierczak", 666)
book4 = Book(library2, 2015, "Anna", "Kot", 231)
book5 = Book(library1, 2019, "ZYX", "XYZ", 455)
employee1 = Employee("Piotr", "XYZ", "2016-11-25", "1998-3-6", "Katowice", "Kilinskiego", "41-200", 602345123)
employee2 = Employee("Rafal", "XYZ", "2016-1-12", "1993-6-1", "Katowice", "Kiepury", "41-200", 602345123)
employee3 = Employee("Alicja", "XYZ", "2012-3-1", "1997-6-12", "Katowice", "1_maja", "41-200", 602345122)
order1 = Order(employee1, student1, [book5, book2], datetime.now())
order2 = Order(employee3, student2, book1, datetime.now())
print(order1)
print(order2)


# zad3

class Property():

    def __init__(self, area, rooms, price, address):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    def __str__(self):
        return f"Property area is {self._area}, it costs {self._price}$."


class House(Property):

    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __str__(self):
        return f"House's plot is {self._plot} m2. It's priced at {self._price}$."


class Flat(Property):

    def __init__(self,area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self):
        return f"Flat is located on {self._floor} floor, it has {self._rooms} room(s)."


house = House(120,7,120000,"XYZ", 500)
flat = Flat(80, 3, 423321,"ZYX", 7)
print(house)
print(flat)
