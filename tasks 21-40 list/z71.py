def generate_2d_array(rows, columns):
    result = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(i * j)
        result.append(row)
    return result

rows = 3
columns = 4

result_array = generate_2d_array(rows, columns)
print("Resulting 2D array:")
for row in result_array:
    print(row)