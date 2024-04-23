def swapletters(a):
    if len(a) < 2:
        return a
    else:
        return a[-1] + a[1:-1] + a[0]

b = "hello"
result = swapletters(b)
print("Original String:", b)
print("String after exchanging first and last characters:", result)