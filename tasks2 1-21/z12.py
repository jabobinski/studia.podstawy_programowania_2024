def abc(s):
    s = s.lower() 
    return s == s[::-1]

a = "madam"
print("Is palindrome: ", abc(a))