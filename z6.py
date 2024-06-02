def student_data(student_id, student_name=None, student_class=None):
    print(f"Student ID: {student_id}")
    
    if student_name is not None:
        print(f"Student Name: {student_name}")
    
    if student_class is not None:
        print(f"Student Class: {student_class}")

student_data(101)
print() 
student_data(102, student_name="Estera")
print() 
student_data(103, student_name="Zuzia", student_class="5th Grade")