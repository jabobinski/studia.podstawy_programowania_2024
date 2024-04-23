def count_characters(string):
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

sample_string = "google.com"
result = count_characters(sample_string)
print("Character frequency:", result)