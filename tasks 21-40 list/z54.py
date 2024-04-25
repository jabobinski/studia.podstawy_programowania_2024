def sort_dict_by_key(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict

my_dict = {'b': 2, 'a': 1, 'c': 3}

sorted_dict = sort_dict_by_key(my_dict)
print("Sorted Dictionary by Key:", sorted_dict)