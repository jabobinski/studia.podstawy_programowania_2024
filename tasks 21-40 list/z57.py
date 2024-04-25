def abc(dictionary):
    unique_dict = {}
    for key, value in dictionary.items():
        if value not in unique_dict.values():
            unique_dict[key] = value
    return unique_dict

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

unique_dict = abc(my_dict)
print("Dictionary after removing duplicates:", unique_dict)