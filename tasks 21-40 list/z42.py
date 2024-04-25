def abc(d, key, value):
    d[key] = value
    return d

a = {0: 10, 1: 20}

new_key = 2
new_value = 30

updated_dict = abc(a, new_key, new_value)
print("Updated Dictionary:", updated_dict)