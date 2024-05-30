def abc(n):
    if n < 0:
        raise ValueError("must be noninteger")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

a = 5
print("Wynik liczby ", a, "to", abc(a))