def reverse_word(word):
    return word[::-1]

user_input = input("Enter a word: ")
reversed_word = reverse_word(user_input)
print("Reversed word:", reversed_word)