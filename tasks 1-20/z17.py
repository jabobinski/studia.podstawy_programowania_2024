def abc(a):
    if len(a) < 2:
        return "Lenght must be > 2"
    else:
        b = a[-2:]
        return b * 4

print(abc('Python')) 
print(abc('Exercises')) 