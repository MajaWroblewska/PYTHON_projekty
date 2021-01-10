'# zad 10'
from functools import reduce

'1. dla podanej listy zwróci liczby podzielne przez 5'

print('Zad 1')
lista1=[2,55,10,95,84,42,32,8,15]
obliczenie=filter((lambda x : x%5==0), lista1)
print('lista1:',lista1)
print('liczby listy podzielne przez 5:',list(obliczenie))
print('---'*30)

sequence = [2,55,10,95,84,42,32,8,15]
mapped = filter(lambda x: x % 5 == 0, sequence)
print('trenera:', list(mapped))
print('***'*30)
################################################################

'2.Dla par liczb w liście [(a,b),(c,d),(e,f)...] zwróci listę sum tych par z których iloczyn jest podzielny przez 5'

print('Zad 2')
lista2=[(2,5),(8,6),(9,8),(10,4),(20,3)]
print('lista2:',lista2)

# obliczenia2= map((lambda x : x[0]+x[1]),lista2)   #lista sum par (a,b)
# lista3=list(obliczenia2)
# print('suma par',lista3)

obliczenia2=filter(lambda x : x[0] * x[1] % 5 == 0, lista2) #lista iloczynów par (a,b)
# print('filtr iloczynów par %5==0:',lista2)

obliczenia3=map((lambda x : x[0]+x[1]), list(obliczenia2))
print('suma par liczb których iloczyn %5==0:', list(obliczenia3))
print('---'*30)

sequence=[(2,5),(8,6),(9,8),(10,4),(20,3)]
# sequence = [(1,2), (2,3), (5,5), (12,0)]
filtered_seqence = filter(lambda x: (x[0] * x[1]) % 5 == 0, sequence)
a = map(sum, filtered_seqence)
print('trenera:', list(a))
print('***'*30)

####################################################################

'3. Dla dowolnego słownika zwróć listę stringów złączonymi za pomocą podkteślnika kluczami i wartościami,/' \
' gdzie klucz zostanie zamieniony na Wielką literę {"klucz":"wartość"} ->["KLUCZ_wartość"]'

print('Zad 3')
slownik = {'key1': '1', 'key2': '2', 'key3': 'None', 'klucz4': 'str'}
print('slownik:', slownik)

list_dict=list(slownik.items()) #zamiana CALEGO slownika na listę -> lista tupli ('key' , 'value')
# print(list_dict)    #-> [('key1', '1'), ('key2', '2'), ('key3', 'None'), ('klucz4', 'str')]

map1=map(lambda x: '_'.join(x), list_dict)  #ale nie jest dużą literą
print('musi być DUŻYMI literą [map1=map(lambda x: "_".join(x), list_dict]: ',list(map1))

map2=map(lambda x: f'{x[0].upper()}_{x[1].lower()}', list_dict)  #ale nie jest dużą literą
print("map2=map(lambda x: f'{x[0].upper()}_{x[1].lower()}', list_dict): ",list(map2))

print("---"*30)
sl = {'key1': '1', 'key2': '2', 'key3': 'None', 'klucz4': 'str'}
sl = [(k, v) for k, v in sl.items()]
print('trener\
-sl = [(k, v) for k, v in sl.items()] ->:',list(map(lambda x: f'{x[0].upper()}_{x[1].lower()}', sl)))
print("***"*30)

'4. za pomocą samego "reduce":zwróć sumę tablicy liczbowej tych elementów które są większe od 10\'' \
'pierwszy - dowolny czyli też do sumy'

print('Zad 4')
lista4=[2,5,6,80,15,10]
print('lista4:',lista4)
big10=filter(lambda x : x > 10, lista4)

sumbig10=reduce((lambda x, y : x + y), list(big10))   #bez sumy pierwszego elemenu
print('(bez pierwszego elementu-suma cyfr listy4 elem>10=', sumbig10)
sumbig10=reduce((lambda x, y : x + (y if y>10 else 0)),lista4)
print('suma cyfr listy4 elem>10=', sumbig10)

from functools import reduce
sequence = [2,5,6,80,15,10]
print('trenera:', reduce(lambda x, y: x + (y if y > 10 else 0), sequence))
