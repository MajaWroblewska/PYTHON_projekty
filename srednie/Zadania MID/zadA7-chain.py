#chain
'czujnik pogordowy zwraca listę krotek w postaci: [("Miejscowość1","pomiar1", "wartość"), ("Miejscowość2","pomiar2", "wartość")...]\
Przygotuj dane testowe i zagreguj dane z kilku czujników pogodowych do listy i użyj "chain"z modułu "itertools" aby wypisać wszystkie pomiary.'

from itertools import chain

lista=[("Bydgoszcz", "Temperatura", '30'),
       ('Wrocław','Opady','22'),
       ("Bydgoszcz", "Wilgotnosc", "60%")
       ]
print('lista:',lista)
print('*'*30)

for elem in chain(lista):
    print('in chain(lista):',elem)
print('*'*30)

for elem in lista:
    print('in lista:',elem)
print('*'*30)

for elem in chain(*lista):
    print('in chain(*lista):',elem)
print('*'*30)

for elem in lista:
    for el in elem:
        print('for for in lista:',el.lower())
print('*'*30)
