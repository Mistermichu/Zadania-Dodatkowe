'''
Popros uzytkownika o podanie dwoch liczb calkowitych.
Sprawdz, czy jedna liczba jest podzielna przez druga bez reszty i wyswietl odpowiedni komunikat na ekranie.
'''

print("Podaj dwie liczby calkowite")
number_1 = None
while not isinstance(number_1, int):
    number_1 = input("Liczba 1.: ")
    try:
        number_1 = int(number_1)
    except ValueError:
        print("Podana wartosc nie jest liczba calkowita! Sprobuj ponownie.")

number_2 = None
while not isinstance(number_2, int):
    number_2 = input("Liczba 2.: ")
    try:
        number_2 = int(number_2)
    except ValueError:
        print("Podana wartosc nie jest liczba calkowita! Sprobuj ponownie.")

if number_1 % number_2 == 0:
    print("Pierwsza liczba jest podzielna przez druga bez reszty")
else:
    print("Pierwsza liczba jest podzielna przez druga z reszta.")
