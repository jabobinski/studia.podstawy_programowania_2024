def obliczanie_licencji(typ_licencji, num_users, czas_trwania, uslugi):
    licencje = {
        "basic": 10,
        "standard": 20,
        "premium": 30
    }
    
    dodatkowe_uslugi = {
        "support": 5,     
        "tools": 10       
    }
    
    koszt = licencje[typ_licencji] * num_users * czas_trwania
    dodatkowe_koszta = sum(dodatkowe_uslugi[dodatek] for dodatek in uslugi if dodatek in dodatkowe_uslugi) * czas_trwania
    suma = koszt + dodatkowe_koszta
    
    return suma

def main():
    print("Zakup licencji.")
    
    typ_licencji = input("Wybierz typ licencji (basic, standard, premium): ").strip().lower()
    
    if typ_licencji not in ["basic", "standard", "premium"]:
        print("Nieprawidłowy typ licencji. Dostępne typy to: basic, standard, premium.")
        return 
    
    num_users = int(input("Podaj liczbę użytkowników: "))
    czas_trwania = int(input("Podaj czas trwania licencji (w miesiącach): "))
    
    uslugi = []
    add_support = input("Czy chcesz wsparcie techniczne? (y/n): ").strip().lower()
    if add_support == 'y':
        uslugi.append("support")
    
    add_tools = input("Czy chcesz dodatkowe narzędzia? (y/n): ").strip().lower()
    if add_tools == 'y':
        uslugi.append("tools")
    
    total_cost = obliczanie_licencji(typ_licencji, num_users, czas_trwania, uslugi)
    
    if total_cost is None:
        print("nieprawidłowy typ licencji.")
        return
    
    print("\nPodsumowanie:")
    print(f"Typ licencji: {typ_licencji.capitalize()}")
    print(f"Liczba użytkowników: {num_users}")
    print(f"Czas trwania licencji: {czas_trwania} miesięcy")
    print(f"Dodatkowe moduły: {', '.join(uslugi) if uslugi else 'Brak'}")
    print(f"Całkowity koszt licencji: {total_cost} PLN")

main()