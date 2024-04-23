def countword(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

sample_sentence = "Sample Sentence with Sample Sentence"
words = countword(sample_sentence)
print("Word Occurrences:", words)