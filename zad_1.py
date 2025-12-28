from classes.student import Student

student_passed = Student("Person1", [70, 60, 80])

student_failed = Student("Person2", [5, 8, 9])

print(f" Has student `{student_passed}` passed? {student_passed.is_passed()}")
print(f" Has student `{student_failed}` passed? {student_failed.is_passed()}")
