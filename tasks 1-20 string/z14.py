def abc(words):
    distinct_words = sorted(set(words))
    print("Words:", ', '.join(distinct_words))

sample_words = input("Enter words: ").split(',')
abc(sample_words)