def count_chars(a):
    char_freq = {}
    for char in a:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

w = "google.com"
b = count_chars(w)
print("Character frequency:", b)