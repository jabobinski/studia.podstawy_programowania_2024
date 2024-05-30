def abc(numbers):
    b = 1
    for number in numbers:
        b *= number
    return b

a = [8, 2, 3, -1, 7]
print("Wynik:", abc(a))