def abc(a):
    if len(a) < 3:
        return a
    else:
        return a[:3]

print(abc('ipy')) 
print(abc('python')) 