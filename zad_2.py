from classes.book import Book
from classes.employee import Employee
from classes.library import Library
from classes.order import Order
from classes.student import Student



lib1 = Library("Kijow", "Podil", "00-000", "07-15", "123456789")
lib2 = Library("Odessa", "Derebasivska", "00-000", "08-16", "987654321")

print(f"Library: {lib1}")



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




b1 = Book(lib1, "1987-09-04", "Haruki", "Murakami", 380)
b2 = Book(lib1, "1954-01-01", "Yukio", "Mishima", 200)
b3 = Book(lib2, "2019-10-01", "Sayaka", "Murata", 160)
b4 = Book(lib2, "1948-06-15", "Osamu", "Dazai", 180)
b5 = Book(lib1, "1935-01-01", "Yasunari", "Kawabata", 150)

print(b1)




student_1 = Student("Student1", [70, 60, 80])
student_2 = Student("Student2", [30, 50, 90])
student_3 = Student("Student3", [10, 20, 70])


order1 = Order(e1, student_1, [b1, b2], "2005-08-20")
order2 = Order(e2, student_2, [b3, b4, b5], "2005-08-10")

print(f"Order1:\n{order1}\n\n")
print(f"Order2:\n{order2}\n\n")
