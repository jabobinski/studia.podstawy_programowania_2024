def clone_list(a):
    return a.copy()

b = [1, 2, 3, 4, 5]
c = clone_list(b)
print("Original list: ", b)
print("Cloned list: ", c)