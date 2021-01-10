# Zad4 Podaj imię i odpowiedz
a=10
name=input('Jak masz na imię?')
print('Nice to meet you',name.title())
print(f'imię {name}') # f string
print(f'napis {name} {a}')

def hello(imie):
    print('Witaj ', imie)


imie = input('Podaj imię:')
hello(imie)