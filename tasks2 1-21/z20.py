def abc():
    x = 10
    y = 20
    z = "hello"
    b = locals()
    a = len(b) - 1  
    return a
ggg = abc()
print("variables:", ggg)