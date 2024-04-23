def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_all_prime(numbers):
    return all(is_prime(num) for num in numbers)

sample_data = [
    [0, 3, 4, 7, 9],
    [3, 5, 7, 13],
    [1, 5, 3]
]

for numbers_list in sample_data:
    print("Prime: ", check_all_prime(numbers_list))