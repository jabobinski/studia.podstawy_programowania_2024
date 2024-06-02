def student(name, age, grade):
    return f"Name: {name}, Age: {age}, Grade: {grade}"

argument_names = student.__code__.co_varnames[:student.__code__.co_argcount]
print("Arguments: ", argument_names)