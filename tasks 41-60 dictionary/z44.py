def abc(dictionary, key):
    if key in dictionary:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

my_dict = {'a': 1, 'b': 2, 'c': 3}

abc(my_dict, 'a') 
abc(my_dict, 'd') 