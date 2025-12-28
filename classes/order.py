from classes.book import Book
from classes.employee import Employee
from classes.student import Student


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
