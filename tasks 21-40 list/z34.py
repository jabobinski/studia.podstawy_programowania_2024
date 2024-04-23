def abc(b):
    return [num for num in b if num % 2 != 0]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = abc(a)
print(d)