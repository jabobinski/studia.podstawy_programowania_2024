def all_digits_even(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True

result = []

for num in range(100, 401):
    if all_digits_even(num):
        result.append(str(num))

print(",".join(result))