def abc(a):
    if len(a) % 4 == 0:
        return a[::-1]
    else:
        return a

print(abc('code')) 
print(abc('study')) 