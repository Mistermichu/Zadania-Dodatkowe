'''
Popros uzytkownika o podanie zdania. 
Nastepnie oblicz i wyswietl liczbe slow w tym zdaniu. 
Zakładamy, że słowa są oddzielone spacjami.
'''
print("Wprowadz zdanie: ")
user_input = input("")
words = user_input.split()
word_lenght = len(words)

print(word_lenght)