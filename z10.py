class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student = Student(1, "Alice")

student.student_class = "5th Grade"

print("Attributes and values before removing student_name:")
print(student.__dict__)

del student.student_name

print("\nAttributes and values after removing student_name:")
print(student.__dict__)