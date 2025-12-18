class Library:
    def __init__(self, city:str, street:str, zip_code:str, open_hours:str, phone:str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.city}, {self.street}, {self.zip_code}, {self.open_hours}, {self.phone}"

lib1 = Library("Kijow", "Podil", "00-000", "8:888-88:88", "123456789")
lib2 = Library("Odessa", "Derebasivska", "00-000", "9:99-99:99", "987654321")

print(lib1)

class Employee:
    def __init__(self, first_name:str, last_name:str, hire_date:str, birth_date:str, city:str, street:str, zip_code:str, phone:str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}, {self.hire_date}, {self.birth_date}, {self.city}, {self.street}, {self.zip_code}, {self.phone}"

e1 = Employee("Katia", "Shevchenko", "2015-01-01", "1995-01-12", "Kijow", "Bromska 3", "00-000", "111222333")
e2 = Employee("Solomia", "Kovalchuk", "2016-01-11", "1992-01-20", "Odessa", "Zuliany 4", "00-000", "444555666")
e3 = Employee("Sofia", "Antonenko", "2017-01-11", "1990-01-10", "Chernohiv", "Kchreshchatyk 8", "00-000", "777888999")

print(e1)

class Book:
    def __init__(self, library:str, publication_date:str, author_name:str, author_surname:str, number_of_pages:str):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"{self.author_name} {self.author_surname} {self.number_of_pages}{self.library}"


b1 = Book(lib1, "1987-09-04", "Haruki", "Murakami", 380)
b2 = Book(lib1, "1954-01-01", "Yukio", "Mishima", 200)
b3 = Book(lib2, "2019-10-01", "Sayaka", "Murata", 160)
b4 = Book(lib2, "1948-06-15", "Osamu", "Dazai", 180)
b5 = Book(lib1, "1935-01-01", "Yasunari", "Kawabata", 150)

print(b1)

class Order:
    def __init__(self, employee:str, student:str, books:str, order_date:str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return f"{self.employee} {self.student} {self.books} {self.order_date}"

order1 = Order(e1, "student1", b1, "2005-08-20")
print(order1)