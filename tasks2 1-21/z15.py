def abc(sequence):
    words = sequence.split('-')
    sorted_words = sorted(words)
    sorted_sequence = '-'.join(sorted_words)
    return sorted_sequence

sample_sequence = "green-red-yellow-black-white"
sorted_sequence = abc(sample_sequence)
print("sorted sequence:", sorted_sequence)