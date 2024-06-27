def get_number_input():
    try:
        num = float(input("Enter a number: "))  # Using float to handle both integers and floats
        return num
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return None

# Example usage:
try:
    number = get_number_input()
    if number is not None:
        print(f"You entered: {number}")
    else:
        print("No input received.")
except KeyboardInterrupt:
    print("\nProgram terminated due to KeyboardInterrupt.")
