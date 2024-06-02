import builtins

abs_function = builtins.abs

print(abs_function.__doc__)

absolute_value = abs_function(-155)
print("value is: ", absolute_value)