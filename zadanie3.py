'''
Popros uzytkownika o podanie dwoch liczb calkowitych.
Sprawdz, czy jedna liczba jest podzielna przez druga bez reszty i wyswietl odpowiedni komunikat na ekranie.
'''

print("Podaj dwie liczby calkowite")
number_1 = None
while number_1 not isinstance(int):
    number_1 = input("Liczba 1.: ")


