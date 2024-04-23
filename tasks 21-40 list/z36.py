def abc():
    square_numbers = []
    for num in range(1, 31):
        if num ** 0.5 == int(num ** 0.5):
            square_numbers.append(num)
    return square_numbers[:5] + square_numbers[-5:]

h = abc()
print(h)