def abc(s):
    a = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    s = ''.join(char for char in s if char.isalpha())
    return all(letter in s for letter in a)

sample_string = "The quick brown fox jumps over the lazy dog"
print("is string panagram: ", abc(sample_string))