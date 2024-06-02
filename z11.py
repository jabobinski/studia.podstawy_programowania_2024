class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None  

    def display_attributes(self):
        print("Attributes and values of the Student:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

student = Student(1, "Alice")

student.student_class = "5th Grade"

student.display_attributes()