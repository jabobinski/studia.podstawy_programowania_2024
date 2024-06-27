def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage:
filename = "nonexistent_file.txt"

read_file(filename)
