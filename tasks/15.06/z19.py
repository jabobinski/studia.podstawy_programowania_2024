def read_file(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except UnicodeDecodeError as ude:
        print(f"Error: Unable to decode file '{filename}' with encoding '{encoding}'.")
        print(f"UnicodeDecodeError: {ude}")

# Example usage:
filename = "example_file.txt"

read_file(filename)
