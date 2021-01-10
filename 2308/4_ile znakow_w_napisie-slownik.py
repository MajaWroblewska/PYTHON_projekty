'''a={}
k=8
a['k']='wartosc1'
a[k]='wartosc2'
a[4]='wartosc3'
print(a)
'''
#słownik co zbiera wystąpienie danego znaku, też znaki białe (+wielkosc znaku nieistotna)(+nie liczy spacje)(-bez białych znaków)
slownik={}
zdanie=input('Wpisz zdanie: ')
begin=1
zdanie=zdanie.lower() #zmienia zmienna zdanie na małe litery

for litera in zdanie:
    if litera in slownik:
        slownik[litera]+=begin #dodawanie wartości kolejnej(=1) do klucza='litera'
    else:
        slownik[litera]=begin #dodaenie nowego klucza(elementu) do słownika

print(slownik)

'''
#KOD Jany
s = 'aaaBbccc de 122333,,'
d = {}
for i in s.lower():
    if i.isalpha():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
print(d)
'''