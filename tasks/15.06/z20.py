def perform_list_operation(input_list):
    try:
        # Attempting to perform a list operation that might raise AttributeError
        length = input_list.length()  # Example: Trying to get the length attribute
        print(f"Length of the list: {length}")
    except AttributeError as ae:
        print(f"Error: {ae}")

# Example usage:
my_list = [1, 2, 3, 4, 5]

# Case 1: Valid operation
perform_list_operation(my_list)  # Trying to get the length of the list

# Case 2: Invalid operation
perform_list_operation(123)  # Trying to get the length of an integer (which does not have a length attribute)
