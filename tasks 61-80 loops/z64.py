def print_pattern(rows):
    for i in range(rows): 
        for j in range(i + 1): 
            print("*", end=" ")
        print() 

    for i in range(rows - 2, -1, -1):
        for j in range(i + 1): 
            print("*", end=" ")
        print() 

print_pattern(5)