def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Division result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ArithmeticError as ae:
        print(f"Arithmetic Error occurred: {ae}")

# Example usage:
try:
    divide_numbers(10, 2)   # Normal division
    divide_numbers(10, 0)   # Division by zero
    divide_numbers(10, '2') # Invalid operation causing ArithmeticError
except ArithmeticError as ae:
    print(f"Arithmetic Error occurred outside function: {ae}")
