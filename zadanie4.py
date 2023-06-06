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
    string_number = str(user_number)
    decimal_index = string_number.index(".")
    user_number = int(user_number)
    decimal_number = string_number[(decimal_index + 1):]
    decimal_number = int(decimal_number)
    bin_number = bin(user_number)[2:]
    bin_decimal_number = bin(decimal_number)[2:]
    bin_number = bin_number + "." + bin_decimal_number
    print(bin_number)
