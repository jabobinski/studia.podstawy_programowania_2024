class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(1, "Alice")
student2 = Student(2, "Bob")

def print_attributes(student):
    print(f"Attributes of {student.__class__.__name__}:")
    for attr, value in student.__dict__.items():
        print(f"{attr}: {value}")

print_attributes(student1)
print()
print_attributes(student2)