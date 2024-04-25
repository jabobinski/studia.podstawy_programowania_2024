class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def obj_to_dict_using_vars(obj):
    return vars(obj)

def obj_to_dict_using_dict_attr(obj):
    return obj.__dict__

person = Person("Alice", 30)

dict_vars = obj_to_dict_using_vars(person)
print("Dictionary created using vars():", dict_vars)

dict_dict_attr = obj_to_dict_using_dict_attr(person)
print("Dictionary created using __dict__ attribute:", dict_dict_attr)