class Student:
    def __init__(self, name: str, marks: list[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50


student_passed = Student("Person1", [70, 60, 80])
student_failed = Student("Person2", [5, 8, 9])

print(f" Has {student_passed.name} paseed? {student_passed.is_passed()}")
print(f" Has {student_failed.name} paseed? {student_failed.is_passed()}")
