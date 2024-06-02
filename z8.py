class Student:
    pass

class Marks:
    pass

student_instance = Student()
marks_instance = Marks()

print("Is student_instance an instance of Student?", isinstance(student_instance, Student))
print("Is marks_instance an instance of Marks?", isinstance(marks_instance, Marks))

print("Is Student a subclass of object?", issubclass(Student, object))
print("Is Marks a subclass of object?", issubclass(Marks, object))