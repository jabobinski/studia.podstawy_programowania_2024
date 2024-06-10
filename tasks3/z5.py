digits_sum = 0
provided_digits_amount = 0
 
while digits_sum < 99:
    user_input = int(input('Podaj liczbę: '))
    if (digits_sum + user_input < 100):
        digits_sum += user_input
        provided_digits_amount += 1
    else:
        print('Zostala przekroczona maksymalna liczba')
        break

print(f'Provided digits amount: {provided_digits_amount}')