def a(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper

def b(func):
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper

def c(func):
    def wrapper(*args, **kwargs):
        return "<u>" + func(*args, **kwargs) + "</u>"
    return wrapper

@a
@b
@c
def greet(f):
    return f"Hello, {f}!"

abc = greet("Alice")
print("Wynik: ", abc)