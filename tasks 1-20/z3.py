def get_first_last_chars(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]

samples = ['w3resource', 'w3', ' w']
for s in samples:
    result = get_first_last_chars(s)
    print("Sample String:", s)
    print("Expected Result:", result)