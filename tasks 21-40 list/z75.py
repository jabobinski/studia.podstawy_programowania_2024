import re

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"
    
    if re.match(pattern, password):
        return True
    else:
        return False

password = input("Enter a password: ")

if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")