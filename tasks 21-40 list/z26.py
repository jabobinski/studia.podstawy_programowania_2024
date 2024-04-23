def abc(a):
    return sorted(a, key=lambda x: x[-1])

b = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
y = abc(b)
print(y)