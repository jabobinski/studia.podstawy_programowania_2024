def abc(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        coefficient = 1
        for j in range(i + 1):
            print(coefficient, end=" ")

            coefficient = coefficient * (i - j) // (j + 1)
        print()

num_rows = 5
abc(num_rows)
