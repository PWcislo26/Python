from datetime import datetime


class Student():

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.marks > 50:
            return True
        return False


student1 = Student("Piotr", 57)
print(student1.is_passed())

student2 = Student("Alicja", 36)
print(student2.is_passed())


class Library():
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"Library in {self.city} on {self.street}"


class Order():
    def __init__(self, employee, student, books, order_date) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return f"Order is being processed by {self.employee} it consits of {}."


class Employee():
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"Employee {self.first_name} {self.last_name} living in {self.city}"


class Book():
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Book written by {self.author_name} {self.author_surname}, currently in {self.library}"


library1 = Library("Katowice", "3_maja", "41-200", "8-16", 602354971)
library2 = Library("Sosnowiec", "XYZ", "42-323", "9-17", 606323953)
book1 = Book(library1, 1964, "Alfred", "XYZ", 543)
book2 = Book(library1, 1999, "Norman", "Nolan", 2211)
book3 = Book(library2, 2005, "Norbert", "Gierczak", 666)
book4 = Book(library2, 2015, "Anna", "Kot", 231)
book5 = Book(library1, 2019, "ZYX", "XYZ", 455)
employee1 = Employee("Piotr", "XYZ", "2016-11-25", "1998-3-6", "Katowice", "Kilinskiego", "41-200", 602345123 )
employee2 = Employee("Rafal", "XYZ", "2016-1-12", "1993-6-1", "Katowice", "Kiepury", "41-200", 602345123 )
employee3 = Employee("Alicja", "XYZ", "2012-3-1", "1997-6-12", "Katowice", "1_maja", "41-200", 602345122 )
order1 = Order(employee1,student1, [book5, book2], datetime.now())
print(order1)