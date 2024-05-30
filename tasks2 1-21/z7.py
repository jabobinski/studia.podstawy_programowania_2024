def abc(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

sample_string = 'The quick Brow Fox'
upper, lower = abc(sample_string)
print("No. of Upper case characters:", upper)
print("No. of Lower case Characters:", lower)