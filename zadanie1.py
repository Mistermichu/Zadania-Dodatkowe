'''
Poproś użytkownika o podanie listy liczb całkowitych oddzielonych spacjami.
Następnie oblicz i wyświetl sumę tych liczb
'''

user_input = input("Wprowadz liczby calkowite oddzielone spacja: ")
number_list = user_input.split()

sum = 0
for calculation in number_list:
    try:
        sum += int(calculation)
    except ValueError:
        print(f"\"{calculation}\" nie jest liczba calkowita!")


print(sum)