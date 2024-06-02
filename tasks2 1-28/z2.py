class abc:
    class_variable = 42

    def __init__(self, value):
        self.instance_variable = value

    def my_method(self):
        return "Hello, World!"

print(dir(abc))

instance = abc(10)
print("Instance namespace:", instance.__dict__)
print("Class namespace:", abc.__dict__)