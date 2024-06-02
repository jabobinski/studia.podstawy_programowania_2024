class MyClass:
    pass

instance = MyClass()

class_name = instance.__class__.__name__

print("Class name of the instance:", class_name)