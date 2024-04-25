def get_max_min_values(dictionary):
    max_value = max(dictionary.values())
    min_value = min(dictionary.values())
    return max_value, min_value

my_dict = {'a': 10, 'b': 5, 'c': 20}

max_value, min_value = get_max_min_values(my_dict)
print("Maximum value:", max_value)
print("Minimum value:", min_value)