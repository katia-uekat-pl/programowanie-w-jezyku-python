class Student:
    def __init__(self, name: str, marks: list[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False
        if len(self.marks) == 0:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50

    def __str__(self) -> str:
        return f"name: {self.name}, marks: {self.marks}"