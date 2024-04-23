import random

def abc(a):
    b = a[:]
    random.shuffle(b)
    return b

d = [1, 2, 3, 4, 5]
b = abc(d)
print(b)