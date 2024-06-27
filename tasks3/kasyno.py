import random
import time

# Symbole dostepne w slotach
symbols = ["7", "A", "B", "C", "D", "J", "$"]

# Generacja maszyny ze slotami 3x3
def generate_board():
    return [[random.choice(symbols) for _ in range(3)] for _ in range(3)]  # Tworzenie planszy 3x3 z losowymi symbolami

# Wyswietlanie slotow 3x3
def display_board(board):
    for row in board:
        print(" | ".join(row))  # Wyświetlanie każdego rzędu z symbolami oddzielonymi "|"
        print("-" * 9)  # Linia miedzy rzędami

# Funkcja obliczająca wygraną na podstawie planszy i stawki
def calculate_winnings(board, bet):
    winnings = 0  # Zmienna od wygranej
    win_indices = set()  # Zbior wygranych symboli

    # Sprawdzenie jackpotu kiedy wszystkie pola to "7"
    if all(symbol == "7" for row in board for symbol in row):
        for i in range(3):
            for j in range(3):
                win_indices.add((i, j))  # Dodanie wszystkich indeksów do zbioru wygranych symboli
        return bet * 100, win_indices  # Zwracanie wygranej i indeksów wygranych symboli
    
    # Sprawdzenie rzędów i kolumn
    for i in range(3):
        # Sprawdzenie rzędów
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "7":
                winnings += bet * 3  # Wygrana dla rzędu z "7"
            elif board[i][0] in "ABCDJ":
                winnings += bet * 0.5  # Wygrana dla rzędu z "A", "B", "C", "D" lub "J"
            elif board[i][0] == "$":
                winnings += bet * 1.5  # Wygrana dla rzędu z "$"
            win_indices.update([(i, 0), (i, 1), (i, 2)])  # Dodanie indeksów wygranych symboli do zbioru

        # Sprawdzenie kolumn
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "7":
                winnings += bet * 3  # Wygrana dla kolumny z "7"
            elif board[0][i] in "ABCDJ":
                winnings += bet * 0.5  # Wygrana dla kolumny z "A", "B", "C", "D" lub "J"
            elif board[0][i] == "$":
                winnings += bet * 1.5  # Wygrana dla kolumny z "$"
            win_indices.update([(0, i), (1, i), (2, i)])  # Dodanie indeksów wygranych symboli do zbioru
    
    return winnings, win_indices  # Zwracanie wygranej i indeksów wygranych symboli

# Funkcja do animacji kręcenia slotów
def spin_animation():
    for _ in range(5):  
        temp_board = generate_board()  
        display_board(temp_board)  # Wyświetlanie tymczasowej planszy
        time.sleep(0.5) 
        print("\033[H\033[J", end="")  # Czyszczenie konsoli

# Funkcja do zaznaczania wygranych symboli
def highlight_winning_symbols(board, win_indices):
    for i, j in win_indices:
        board[i][j] = f"[{board[i][j]}]"  # Oznaczanie wygranych symboli nawiasami kwadratowymi
    return board  # Zwracanie zmodyfikowanej planszy

# Funkcja główna obsługująca interfejs kasyna
def casino():
    balance = float(input("Wprowadź ilość pieniędzy, którą chcesz wpłacić na swoje konto: ")) 
    bet = float(input("Wprowadź stawkę, którą chcesz postawić: ")) 
    
    while True:
        print(f"\nTwoje saldo: {balance:.2f} PLN") 
        
        if bet > balance:
            print("Nie masz wystarczająco pieniędzy, aby postawić taką stawkę.")  
            continue
        
        print("\nKręcenie slotów...")
        spin_animation()  # Uruchamianie animacji kręcenia slotów
        
        board = generate_board()  # Generowanie finalnej planszy
        winnings, win_indices = calculate_winnings(board, bet)  # Obliczanie wygranej i wygranych symboli
        balance += winnings - bet  # Aktualizowanie salda gracza
        loss = bet - winnings  # Obliczanie przegranej kwoty
        
        board = highlight_winning_symbols(board, win_indices)  # Oznaczanie wygranych symboli
        print("\nWynik losowania:")
        display_board(board)  # Wyświetlanie finalnej planszy
        
        print(f"\nWygrana: {winnings:.2f} PLN")  # Wyświetlanie wygranej kwoty
        if winnings < bet:
            print(f"Przegrałeś: {loss:.2f} PLN")  # Wyświetlanie przegranej kwoty, jeśli jest niższa od stawki
        print(f"Nowe saldo: {balance:.2f} PLN")  # Wyświetlanie nowego salda
        
        if balance <= 0:
            print("Nie masz więcej pieniędzy. Gra zakończona.")  # Sprawdzanie czy gracz ma jeszcze pieniądze
            break
        
        cont = input("Czy chcesz zagrać ponownie? (Y/N/B): ").strip().upper()  # Pytanie o kontynuację gry
        if cont == 'N':
            print("Dziękujemy za grę!")  # Zakończenie gry
            break
        elif cont == 'B':
            bet = float(input("Wprowadź nową stawkę, którą chcesz postawić: "))  # Zmiana stawki

casino() 
