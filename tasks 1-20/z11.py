def remove(b):
    return b[::2]

a = "hello"
result = remove(a)
print("Original String:", a)
print("String after removing characters with odd index values:", result)