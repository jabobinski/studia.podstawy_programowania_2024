def abc(a):
    return list(set(a))

b = [1, 2, 3, 3, 4, 5, 5, 6]
c = abc(b)
print(c)