# kalkulator w funkcji NAJ

def calculator(a,b,znak="+"):   #można dać domyślne zmienne np. def calculator2(a, b=2, znak='+'):/
                                # wywołanie wówczas to: calculator(a) bo b=2 i znak='+'

    if znak=="+" or znak=='':
        wynik=a+b
    elif znak=="-":
        wynik=a-b
    elif znak=="*":
        wynik=a*b
    elif znak=="/" or znak==':': #bez znak=='/' każdy znak wpisany spowoduje dzielenie bo logicznie
        wynik=a/b
    elif znak=="%":
        wynik=a%b
    else:
        wynik='Błędny znak'
    return wynik

a=int(input('Podaj liczbę1: '))
b=int(input('Podaj liczbę2: '))
znak=input('Podaj znak operacji: ')

print('Wynik działania:',znak,'to: ',calculator(a,b,znak)) # wywołanie funkcji 'calculator'
print('wynik calculatora (domyśłnie SUMA)to: ', calculator(a,b)) #calculator z domyślnym znakiem"+"


'''
def calculator2(liczba2, liczba1=2, znak='+'):
    if znak == '+':
        wynik = liczba1 + liczba2
    elif znak == '*':
        wynik = liczba1 * liczba2
    else:
        wynik = 'blad'
    return wynik
a = int(input('liczba 1: '))
b = int(input('liczba 2: '))
c = input('dzialanie: ')
print('wynik calculatora to: ', calculator2(a, b, c))
calculator_wynik = calculator2(a, b, c)
print('wynik calculatora to: ', calculator2(a)) #wywołanie z domyślnymi danymi b=2 znak="+
'''