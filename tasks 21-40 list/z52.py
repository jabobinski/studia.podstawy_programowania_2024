def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        print(f"The key '{key}' has been removed from the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

my_dict = {'a': 1, 'b': 2, 'c': 3}

remove_key(my_dict, 'b') 
print("Updated Dictionary:", my_dict)