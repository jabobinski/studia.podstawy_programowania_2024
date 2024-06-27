def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.replace(" ", "").lower()  
    return s == s[::-1]

def main():
    user_input = input("Enter a string to check if it is a palindrome: ")
    
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()
