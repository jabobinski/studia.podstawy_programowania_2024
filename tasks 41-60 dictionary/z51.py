def multiply_dictionary(dictionary):
    result = 1
    for value in dictionary.values():
        result *= value
    return result

my_dict = {'a': 2, 'b': 3, 'c': 4}

total_product = multiply_dictionary(my_dict)
print("Total product of values in the dictionary:", total_product)