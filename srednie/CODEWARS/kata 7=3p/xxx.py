#slownik-wartosc liter
import string
my_list = input('Podaj napis')
# my_list = ["abc","abc","abc","abc"]
slownik_liter={}

def alfabet():
    for i,litera in enumerate(string.ascii_lowercase):
        # print(i)
        slownik_liter[litera]=i+1  #zamiana litery z jej indeksem
    # print(slownik_liter)
    return slownik_liter

k=alfabet()  #fun. słownik wstawiam w zmienna k
print(k)
# print(k['w']) #wartośc znaku w

def suma_slowa():
    suma=0
    for i,znak in enumerate(my_list): #wypisanie wartosci dla my_list wpisanego
        # print(k[znak])
        if znak.isalpha(): #czy znak w my_list jest literą
            suma=suma+k[znak]
        else:
            continue
    return suma

print(suma_slowa())

def wiele_slow():
    for index,slowo in enumerate(my_list):
        suma=suma_slowa()
        suma=suma*(index+1)
    return suma

print(wiele_slow())




f'''or i,x in enumerate(string.ascii_lowercase):
     print(i+1,x)

#print(type(ord('a')))
def wartosc_liter():
    for litera in my_list:
        value=ord(litera)-96
        if value<1 or value>26:
            value=0
            print(value)
        else:
            print(value)
    return value
wartosc_liter()

def zliczanie():
    for litera in my_list:
        print(wartosc_liter(my_list))

zliczanie()'''


