def abc(lst):
    c = [num for num in lst if num % 2 == 0]
    return c

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = abc(b)
print("Lista:", a)