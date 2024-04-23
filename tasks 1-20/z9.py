def abc(input_string, n):
    if n < 0 or n >= len(input_string):
        return "Invalid index"
    else:
        return input_string[:n] + input_string[n+1:]

input_string = "hello"
n = 2
result = abc(input_string, n)
print("Original String:", input_string)
print("String after removing character at index", n, ":", result)