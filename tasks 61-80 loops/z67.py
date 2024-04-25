def print_item_and_type(datalist):
    for item in datalist:
        print(f"Item: {item}, Type: {type(item)}")

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

print_item_and_type(datalist)