class StringReverser:
    def reverse_words(self, s):
        words = s.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

c = StringReverser()
abc = 'hello .py'
print(c.reverse_words(abc)) 