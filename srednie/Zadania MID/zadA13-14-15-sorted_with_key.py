'''sotrt z kluczem'''
from statistics import mean
from typing import List #właczenie typownia
'''zad 13
Sprawdź jak zostanie posortowana lista  [(1, 2, 3), (6, 6, 6), (4, 9, 10), (12, 1, 0), (3, 50, 50)]
1. Posortuj listę wg ostatniego elementu każdej krotki
2. Posortuj listę wg sumy każdej krotki'''
lista = [(1, 2, 3), (6, 6, 6), (4, 9, 10), (12, 1, 0), (3, 50, 50)]
sort1= sorted(lista, key=lambda x: x[2])
sort2= sorted(lista, key=sum)
# sort2= sorted(lista, key=lambda x: x[0]+x[1]+x[2]) #to samo jw
sort3= sorted(lista, key=lambda x: x[0]-x[1]-x[2])
print('ZAD 13')
print('lista:', lista)
print('1-wg ostatniego elementu=',sort1)
print('2-wg sumy krotki=',sort2)
print('3-wg różnicy krotki=',sort3)
print('**'*30)

'''zad14
Listę zawierającej krotki o różnej długości
 posortuj wg średniej wartości elementów.'''

print('ZAD 14')
sample_list=[(1, 2, 3,8,9,550), (6, 6, 6), (4, 9, 10,5), (12, 1), (3, 50, 50)]
posortowana1= sorted (sample_list, key= lambda x:mean(x)) #sort wg średniej wartości
posortowana2= sorted (sample_list, key= mean, reverse=True) #wg sredniej ale odwrotnie
sr= sorted(sample_list,reverse=True, key=len)
print('1-wg średniej rosnąco  :',posortowana1)
print('2-wg średniej malejaco :',posortowana2)
print('3-wg długości malejąco :', sr)

lista=[(1,2),(1,2,3,5,0)]
print(mean(lista[1]))
print(mean(lista[0]))
# mean-średnia wartość

a=[2,8]
b=(2,8)
print('średnia [2,8]=',mean(a))
print('średnia (2,8)=',mean(b))
print('**'*30)

'''zad15
Posortuj tablicę stringów wg ich długości.'''

print('ZAD 15')
tablica=['as', 'ertt','q','12345','wro']
posort= sorted(tablica, key=len)
print('tabica   :',tablica)
print('sort wg długości:',posort)
print('**'*30)


