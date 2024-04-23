def count_chars(string):
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

website = "google.com"
result = count_chars(website)
print("Character frequency:", result)