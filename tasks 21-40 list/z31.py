def abc(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 9]

print("Common member: ", abc(list1, list2))