class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

student_instance = Student("Alice", 101)

print("Type of Student class:", type(Student))

print("Keys of __dict__ attribute of Student class:", Student.__dict__.keys())

print("Value of __module__ attribute of Student class:", Student.__module__)