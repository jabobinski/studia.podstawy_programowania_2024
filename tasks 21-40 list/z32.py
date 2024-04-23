def abc(g):
    a = [0, 4, 5]
    return [g[i] for i in range(len(g)) if i not in a]

b = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
f = abc(b)
print(f)