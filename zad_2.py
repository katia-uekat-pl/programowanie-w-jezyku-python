from zad_1 import Student


class Library:
    def __init__(
            self, city: str, street: str, zip_code: str,
            open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"city: {self.city}, street: {self.street}, zip: {self.zip_code}, "
            f"open: {self.open_hours}, phone: {self.phone}"
        )


lib1 = Library("Kijow", "Podil", "00-000", "07-15", "123456789")
lib2 = Library("Odessa", "Derebasivska", "00-000", "08-16", "987654321")

print(f"Library: {lib1}")


class Employee:
    def __init__(
            self, first_name: str, last_name: str, hire_date: str,
            birth_date: str, city: str, street: str, zip_code: str,
            phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"first: {self.first_name}, last: {self.last_name}, "
            f"hire: {self.hire_date}, "
            f"birth: {self.birth_date}, city: {self.city}, "
            f"street: {self.street}, "
            f"zip: {self.zip_code}, phone: {self.phone}"
        )


e1 = Employee(
    "Katia", "Shevchenko", "2015-01-01", "1995-01-12",
    "Kijow", "Bromska 3", "00-000", "111222333"
)
e2 = Employee(
    "Solomia", "Kovalchuk", "2016-01-11", "1992-01-20",
    "Odessa", "Zuliany 4", "00-000", "444555666"
)
e3 = Employee(
    "Sofia", "Antonenko", "2017-01-11", "1990-01-10",
    "Chernohiv", "Kchreshchatyk 8", "00-000", "777888999"
)

print(e1)


class Book:
    def __init__(
            self, library: Library, publication_date: str, author_name: str,
            author_surname: str, number_of_pages: str):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return (
            f"author name: {self.author_name}, "
            f"author surname: {self.author_surname}, "
            f"pages: {self.number_of_pages}, library: `{self.library}`"
        )


b1 = Book(lib1, "1987-09-04", "Haruki", "Murakami", 380)
b2 = Book(lib1, "1954-01-01", "Yukio", "Mishima", 200)
b3 = Book(lib2, "2019-10-01", "Sayaka", "Murata", 160)
b4 = Book(lib2, "1948-06-15", "Osamu", "Dazai", 180)
b5 = Book(lib1, "1935-01-01", "Yasunari", "Kawabata", 150)

print(b1)


class Order:
    def __init__(self, employee: Employee, student: Student,
                 books: list[Book], order_date: str
                 ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return (f"employee: `{self.employee}`,\n"
                f"student: `{self.student}`,\n"
                f"books: [\n\t{"\n\t".join(map(str, self.books))}\n],\n"
                f"order date: {self.order_date}")


student_1 = Student("Student1", [70, 60, 80])
student_2 = Student("Student2", [30, 50, 90])
student_3 = Student("Student3", [10, 20, 70])


order1 = Order(e1, student_1, [b1, b2], "2005-08-20")
order2 = Order(e2, student_2, [b3, b4, b5], "2005-08-10")

print(f"Order1:\n{order1}\n\n")
print(f"Order2:\n{order2}\n\n")
