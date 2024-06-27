def get_numerical_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)  # Try converting input to float (can handle integers too)
            return number
        except ValueError:
            print("Error: Please enter a valid numerical value.")

def get_two_numerical_inputs():
    while True:
        try:
            num1 = get_numerical_input("Enter the first number: ")
            num2 = get_numerical_input("Enter the second number: ")
            return num1, num2
        except TypeError:
            print("Error: Please enter numerical values for both inputs.")

# Example usage:
try:
    number1, number2 = get_two_numerical_inputs()
    print(f"You entered: {number1} and {number2}")
except TypeError as te:
    print(te)
