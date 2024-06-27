def perform_operation_on_list(input_list, index):
    try:
        result = input_list[index] * 2  # Example operation (multiply by 2)
        print(f"Result of operation: {result}")
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")

# Example usage:
my_list = [1, 2, 3, 4, 5]

# Case 1: Valid index
perform_operation_on_list(my_list, 2)  # Index 2 is valid

# Case 2: Invalid index
perform_operation_on_list(my_list, 10)  # Index 10 is out of range
