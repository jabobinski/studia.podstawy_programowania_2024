import os

def file_exists(directory, filename):
    """Check if a file exists in the specified directory."""
    filepath = os.path.join(directory, filename)
    return os.path.exists(filepath) and os.path.isfile(filepath)

def main():
    directory = input("Enter the directory path: ")
    filename = input("Enter the file name: ")

    if file_exists(directory, filename):
        print(f"The file '{filename}' exists in the directory '{directory}'.")
    else:
        print(f"The file '{filename}' does not exist in the directory '{directory}'.")

if __name__ == "__main__":
    main()
