def are_lists_equal(lst1, lst2):
    """Check if two lists are equal."""
    return lst1 == lst2

def main():
    try:
        print("Enter numbers for the first list:")
        list1 = [int(input(f"Enter number {i + 1}: ")) for i in range(3)]
        print("Enter numbers for the second list:")
        list2 = [int(input(f"Enter number {i + 1}: ")) for i in range(3)]

        if are_lists_equal(list1, list2):
            print("The lists are equal.")
        else:
            print("The lists are not equal.")
    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == '__main__':
    main()
