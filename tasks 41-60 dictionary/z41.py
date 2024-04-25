def abc(d, ascending=True):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))
    return sorted_dict

a = {'a': 4, 'b': 2, 'c': 1, 'd': 3}

ascending_sorted_dict = abc(a, ascending=True)
print("Ascending order:", ascending_sorted_dict)

descending_sorted_dict = abc(a, ascending=False)
print("Descending order:", descending_sorted_dict)