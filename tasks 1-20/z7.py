def replace_not_poor(input_string):
    not_index = input_string.find('not')
    poor_index = input_string.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return input_string[:not_index] + 'good' + input_string[poor_index + 4:]
    else:
        return input_string

sample_strings = ['The lyrics is not that poor!', 'The lyrics is poor!']
for string in sample_strings:
    result = replace_not_poor(string)
    print("Sample String:", string)
    print("Expected Result:", result)