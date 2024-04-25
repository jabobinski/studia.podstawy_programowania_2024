def map_lists_to_dict(keys, values):
    return dict(zip(keys, values))

keys = ['a', 'b', 'c']
values = [1, 2, 3]

result_dict = map_lists_to_dict(keys, values)
print("Mapped Dictionary:", result_dict)