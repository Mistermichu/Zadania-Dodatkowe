'''
Popros uzytkownika o podanie liczby w systemie dziesietnym.
Nastepnie przelicz te liczbe na system dwojkowy i wyswietl wynik na ekranie
'''

user_number = None
while not isinstance(user_number, (int, float)):
    user_number = input("Wprowadz liczbe: ").replace(",", ".")
    try:
        user_number = int(user_number)
    except ValueError:
        try:
            user_number = float(user_number)
        except ValueError:
            print("Podana wartosc nie jest liczba! Sprobuj ponownie")

if isinstance(user_number, int):
    bin_number = bin(user_number)[2:]
    print(bin_number)
else:
    print("Liczba z przecinkiem")
