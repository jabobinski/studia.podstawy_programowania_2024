def replace(b):
    c = b[0]
    d = c + b[1:].replace(c, '$')
    return d

a = 'restart'
result = replace(a)
print("Sample String:", a)
print("Expected Result:", result)