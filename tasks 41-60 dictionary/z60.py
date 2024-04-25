abc = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"}
]

def distinct_values(data):
    unique_values = set()
    for d in data:
        for value in d.values():
            unique_values.add(value)
    return unique_values

distinct = distinct_values(abc)
print("Unique Values:", distinct)