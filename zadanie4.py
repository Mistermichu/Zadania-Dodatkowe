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
    decimal_part = (user_number - int(user_number))
    decimal_part = str(decimal_part)
    decimal_part = decimal_part[2:]
    decimal_part = int(decimal_part)
    bin_number = bin(int(user_number))[2:]
    bin_decimal_part = bin(decimal_part)[2:]
    bin_number = bin_number + "." + bin_decimal_part
    print(bin_number)
