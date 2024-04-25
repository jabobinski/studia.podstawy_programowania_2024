def abc(n):
    square_dict = {}
    for x in range(1, n+1):
        square_dict[x] = x * x
    return square_dict

n = 5
result_dict = abc(n)
print("Sample Dictionary (n =", n, "):")
print("Expected Output:", result_dict)