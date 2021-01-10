#zad 9
'Funkcja która skraca tekst do pierwszych n-znaków i dodaje "...czytaj dalej" \
tekst1- n>len(tekst) wypisuje cały tekst+ ...czytaj dalej \
tekst2 - n>len(tekst) wypisuje tylko cały tekest'
text='123456789abcdefg30'
s=lambda n, tekst : tekst[:n]+'...czytaj dalej'
print('tekst 1:',s(30, text))
#
b=lambda n,tekst : f'{tekst[:n]}...czytaj dalej' if len(tekst)>n else tekst
print('tekst2:',b(5,'aadsddff50'))
print('*'*30)
#
a = lambda x: x * 10
print('wielokrotność 10:',a(50))
#
b = lambda x, y : x * y
print('iloczyn 2-ch liczb',b(5, 7))
#
a=False
b=2 if a else 0
print('1-szybka pętla if:',b)
#
if a:
    b=2
else:
    b=0
print('2-normalna pętla if:',b)
print('*'*30)
#################################################################
'lambda-map-filter-reduce'
from functools import reduce    #do funkcji 'reduce'

# map-
# wykonuje f-cje na wskazanej liście/string
# wynik musi być wymuszony przez 'LIST(wynik)' lub TUPLE(wynik) lub SET(wynik)!!!!
# bez tego pokarze adres obiektu map

sequence = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
print('lista do operacji "sequence":',sequence)
# sequence2=[2,3]
mapped = map(lambda x: x*x, sequence)   #na zbiorze sequence
print('map-cała lista x*x:',list(mapped)) #działa albo linia 35 albo 36 -razem nie dziła ->list index out of range
# print('map-elem[0] x*x:',list(mapped)[0])
#
for i, el in enumerate(sequence):
    sequence[i]=el*el
print('to samo co map ale w pętli for, x*x:',sequence)
print('*'*30)

# map na stringu
#
tekst='dsdsssfdsfdsf'
mapped2=list(map(lambda x: x*2, tekst))
tekst='- '.join(mapped2)
print('podwajani liter dict:',dict(mapped2))
print('podwajani liter set:',set(mapped2))
print('podwajani liter list:',list(mapped2))
print('podwajani liter str:',str(mapped2))
print('podwajanie liter i join(- ):',tekst)
print('*'*30)

# map na 2 listach
# listy musza być równoliczne
# jeżeli nie to nowa lista będzie długości najkrótszej listy- gubimy elementy
lista1 = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
lista2 = [2, 3, 8, 1, 6, 9, 12, 62, 8, 7]
mapped = map((lambda x, y: x * y), lista1,lista2)
print('lista1=',lista1)
print('lista2=',lista2)
print('map na 2 listach lista1[i]*lista2[i]:',list(mapped))
# print('mnozenie list',lista1*lista2)  # nie da się - generuje błąd
print('*'*30)

###################################################################

#filter
# -wykona f-cję i wyfiltruje nam wyniki
filtered = filter(lambda x: x < 5, sequence)
print('lista do operacji "sequence":',sequence)
print('filtracja x<5:',list(filtered))
print('*'*30)

sequence2 = [10,2,8,7,5,4,3,11,0, 1]
print('lista do operacji "sequence2":',sequence2)
filtered2= filter(lambda x : x*2>10, sequence2)
print('filtracja x*2>10:',list(filtered2))
print('*'*30)
#

#reduce - każdy el z każdym
from functools import reduce
sequence = [10,2,8,7,5,4,3,11, 1]
product = reduce((lambda x,y: x*y), sequence)
product2= reduce((lambda x,y :x+y),sequence)
print('lista obliczeniowa:', sequence)
print('reduce x*y',product)
print('reduce x+y', product2)

product = reduce((lambda x, y: max(x,y)), sequence)
print('reduce Max(lista):',product)

