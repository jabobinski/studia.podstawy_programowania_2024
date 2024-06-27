def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Division result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage:
a = 10
b = 0

divide_numbers(a, b)
