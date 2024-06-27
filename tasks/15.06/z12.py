def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Error: Please enter a valid integer.")

# Example usage:
try:
    num = get_integer_input("Enter an integer: ")
    print(f"You entered: {num}")
except ValueError as ve:
    print(ve)
