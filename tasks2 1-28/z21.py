class StringManipulator:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print("String in uppercase:", self.string.upper())

string_manipulator = StringManipulator()
string_manipulator.get_string()
string_manipulator.print_string()