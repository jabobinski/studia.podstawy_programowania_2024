counter = 0
even_counter = 0
arr = []
 
while (counter < 10):
    user_input = int(input('Podaj liczbę: '))
    arr.append(user_input)
    counter += 1
 
for digit in arr:
    if (digit % 2 == 0):
        even_counter += 1
 
print(f'Lista: {arr}')
print(f'Ilość liczb parzystych: {even_counter}')