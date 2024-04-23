def abc(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

h = ['abc', 'xyz', 'aba', '1221']
result = abc(h)
print(result)