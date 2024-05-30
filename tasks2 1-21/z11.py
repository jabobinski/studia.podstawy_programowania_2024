def abc(a):
    if a <= 1:
        return False
    b = 1
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            b += i
            if i != a // i:
                b += a // i
    return b == a

c = 28
print("Is", c, "a perfect number?", abc(c))
