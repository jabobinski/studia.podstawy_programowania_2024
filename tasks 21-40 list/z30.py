def abc(words, n):
    return [word for word in words if len(word) > n]

a = ['piza', 'salami', 'italy', 'spaghetti', 'mozarella']
n = 5
g = abc(a, n)
print(g)