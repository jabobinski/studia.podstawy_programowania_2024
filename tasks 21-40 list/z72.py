print("text:")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line.lower())

print("Lines in lowercase:")
for line in lines:
    print(line)