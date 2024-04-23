def add_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"

print(add_tags('i', 'Python')) 
print(add_tags('b', 'Python Tutorial')) 