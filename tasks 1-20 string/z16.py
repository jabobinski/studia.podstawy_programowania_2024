def abc(a, b):
    c = len(a) // 2
    return a[:c] + b + a[c:]

print(abc('[[]]<<>>', 'Python')) 
print(abc('{{}}', 'PHP')) 