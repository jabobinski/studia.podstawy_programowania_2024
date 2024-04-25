d = {'a': 1, 'b': 2, 'c': 3}

print("Iterating over keys:")
for key in d:
    print(key)

print("\nIterating over values:")
for value in d.values():
    print(value)

print("\nIterating over key-value pairs:")
for key, value in d.items():
    print(key, "->", value)