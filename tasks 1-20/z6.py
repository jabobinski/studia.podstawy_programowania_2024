def abc(input_string):
    if len(input_string) < 3:
        return input_string
    elif input_string.endswith('ing'):
        return input_string + 'ly'
    else:
        return input_string + 'ing'

sample_strings = ['abc', 'string']
for string in sample_strings:
    result = abc(string)
    print("Sample String:", string)
    print("Expected Result:", result)