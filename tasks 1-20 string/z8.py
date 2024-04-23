def longer(words):
    longest_word = ''
    max_length = 0
    
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    
    return longest_word, max_length

word_list = ['Python', 'code', 'Exercises', 'are', 'fun']
longest_word, length = longer(word_list)
print("Longest word:", longest_word)
print("Length of the longest word:", length)