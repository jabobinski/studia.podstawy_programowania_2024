def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to open file '{filename}'.")

# Example usage:
filename = "example_file.txt"

read_file(filename)
