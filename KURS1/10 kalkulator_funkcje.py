# zad 11 kalkulator2
def dodaj(a,b):
    suma=a+b
    print(suma)
    return suma
def odejmij(a,b):
    roznica=a-b
    print(roznica)
    return roznica
def mnoz(a,b):
    iloczyn=a*b
    print(iloczyn)
    return iloczyn
def dziel(a,b):
    iloraz=a/b
    print(iloraz)
    return iloraz
a=float(input('Podaj a: '))
b=float(input('Podaj b: '))
znak=input('Podaj działanie jakie mam wykonać na tych liczbach! ')

if znak=='+':
    print('Suma: ',dodaj(a,b))   #wywołanie funkcji przez print
elif znak=='-':
    print('Róznica: ',odejmij(a,b))
elif znak=='*':
    print('Iloczyn: ',mnoz(a,b))
elif znak=='/' or znak==':':
    print('Iloraz: ', dziel(a,b))
else:
    print('Zły znak')

# wywołanie funkcji
# dodaj(1,2)
# odejmij(8,1)
# mnoz(10,8)
# dziel(4,8)
# print(dodaj(a,b)  #przez print

'''
# krótki kalkulator 
def calc(a,b,znak):
    if znak=="+":
        wynik=a+b
        return wynik
    elif znak=='*':
        wynik=a*b
        return wynik


a=int(input('a:'))
b=int(input('b:'))
znak=input('działanie')
print(calc(a,b,znak))
'''
