class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

student = Student("Alice", 85)

print("Original values:")
print("Student Name:", student.student_name)
print("Marks:", student.marks)

student.student_name = "Bob"
student.marks = 95

print("\nModified values:")
print("Student Name:", student.student_name)
print("Marks:", student.marks)