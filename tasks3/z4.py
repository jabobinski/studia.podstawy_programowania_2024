counter = 0
even_counter = 0
 
while (counter < 10):
    user_input = int(input('Podaj całą liczbę: '))
    if (user_input % 2 == 0):
        even_counter += 1
    counter += 1
print(f'Ilosc parzystych liczb to: {even_counter}')