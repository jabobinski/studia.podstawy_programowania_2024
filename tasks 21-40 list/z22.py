def abc(c):
    a = 1
    for b in c:
        a *= b
    return a

d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total_product = abc(d)
print(total_product)