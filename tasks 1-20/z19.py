def abc(a, b):
    index = a.rfind(b)
    if index == -1:
        return "Specified character not found in the string"
    else:
        return a[:index]

c = "https://www.w3resource.com/python-exercises"
d = "https://www.w3resource.com/python"
b = '/'

print(abc(c, b))
print(abc(d, b)) 