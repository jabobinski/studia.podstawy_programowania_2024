def outer_function():
    def inner_function():
        print("inner function")

    print("outer function")
    inner_function() 

outer_function()