def is_sorted(lst):
    """Check if a list is sorted in ascending order."""
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def main():
    try:
        numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(4)]

        if is_sorted(numbers):
            print("The numbers are in ascending order.")
        else:
            print("The numbers are not in ascending order.")
    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
