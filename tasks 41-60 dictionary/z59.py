from collections import Counter

def combine_dicts(d1, d2):
    combined_dict = Counter(d1)
    combined_dict.update(d2)
    return combined_dict

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = combine_dicts(d1, d2)
print("Combined Dictionary:", combined_dict)