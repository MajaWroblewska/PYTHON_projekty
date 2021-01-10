import string

def kwadratowanie():
    wynik = [x**2 for x in range(101)]
    print(wynik)

kwadratowanie()


def wartosc_slowa(slowo):
    a = [ord(x) for x in slowo]
    print(a)

wartosc_slowa('Powerslave')


def setowanie(slowo):
    a = {ord(x) for x in slowo}
    print(a)

setowanie('Powerslave')


def slownikowanie(slowo, klucz):
    a = {x:ord(x) for i, x in enumerate(slowo)}
    print(a)
    print(f'wartosc klucza {klucz}: {a[klucz]}')

slownikowanie('powerslave', 'p')