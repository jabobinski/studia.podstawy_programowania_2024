class abc:
    class_variable = 42

    def __init__(self, value):
        self.instance_variable = value

    def my_method(self):
        return "Hello World!"

instance = abc(10)

print(instance.__dict__)