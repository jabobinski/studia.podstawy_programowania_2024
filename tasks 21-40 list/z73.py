def divisible_by_5(binary_numbers):
    result = []
    numbers = binary_numbers.split(',')
    for num in numbers:
        decimal_num = int(num, 2)
        if decimal_num % 5 == 0:
            result.append(num)
    return result

binary_numbers = "0100,0011,1010,1001,1100,1001"

divisible_numbers = divisible_by_5(binary_numbers)
print("Numbers divisible by 5:", ",".join(divisible_numbers))