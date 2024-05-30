def abc(lst):
    return list(set(lst))

a = [1, 2, 3, 3, 3, 3, 4, 5]
b = abc(a)
print("Lista:", b)