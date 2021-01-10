'''ZAD 17
Itertools: groupby
1. Dodaj do końca listy z powyższego przykładu kolejny owoc ("fruit", "apple") - dwa razy ten
sam i sprawdź rezultat wykonania programu.
2. Posortuj listę i korzystając napisanej już pętli utwórz słownik z listą produktów w każdej
grupie. Doklej "s" do każdego klucza {"fruits": {"orange", "banana", "apple"},
"drinks": {"tea", "beer"}}
3. Użyj metody groupby do utworzenia słownika z liczbą wystąpień danej grupy w kolekcji. Jak
wyglądałby kod bez użycia tej metody? Zachowaj kod do późniejszego porównania, gdy
poznamy z klasę Counter i Defaultdict.'''

from itertools import groupby

print('ZAD 17')
menu1 = [("fruit", "orange"),
        ("fruit", "banana"),
        ('fruit','apple'),
        ('fruit','apple'),
        ("drink", "beer"),
        ("drink", "tea"),
        ('fruit', 'apple'),
        ('fruit', 'apple')]

for name1, group1 in groupby(menu1, lambda x: x[0]): # lambda x: x[0] -> name =1element krotki / lambda x: x[1] -> name =2element krotki
    print('name1:',name1)
    print('group1:',list(group1))
print('**'*30)

menu2 = [("fruit", "orange"),
        ("fruit", "banana"),
        ('fruit','apple'),
        ('fruit','apple'),
        ("drink", "beer"),
        ("drink", "tea"),
        ('fruit', 'apple'),
        ('fruit', 'apple')]
print('nie posortowane lista z groupby')
for name2, group2 in groupby(menu2, lambda x: x[0]):
    print(name2)
    print(list(group2))
print('**'*30)

print('posortowane lista z groupby')
print('menu prze sortowaniem:',menu2)
menu3=sorted(menu2,) #DOMYŚLNIE wg. 1-elementu= key=lambda  x: x[0])
print('menu po sortowaniu:',menu3)
for name3, group3 in groupby(menu3, lambda x: x[0]):
    print(name3)
    print(list(group3))
print('**'*30)
###############################################################################################################
menu1 = [("fruit", "orange"),
         ("fruit", "banana"),
         ('fruit', 'apple'),
         ('fruit', 'apple'),
         ("drink", "beer"),
         ("drink", "tea"),
         ('fruit', 'apple'),
         ('fruit', 'apple')]
print('1. Dodaj do końca listy z powyższego przykładu kolejny owoc \n("fruit", "apple") - dwa razy ten sam i sprawdź rezultat wykonania programu.')
print('menu1=:', menu1)
for name1, group1 in groupby(menu1, lambda x: x[0]):  # lambda x: x[0] -> name =1element krotki / lambda x: x[1] -> name =2element krotki
    print('name1:', name1)
    print('group1:', list(group1))
print('**' * 30)

print('2. Posortuj listę i korzystając napisanej już pętli utwórz słownik z listą produktów w każdej grupie.\n '
      'Doklej "s" do każdego klucza {"fruits": {"orange", "banana", "apple"}, "drinks": {"tea", "beer"}}')
menu1 = sorted(menu1)
for name, group in groupby(menu1, lambda x: x[0]):
    pusty = []
    for i in group:
        pusty.append(i[1])
        # print(i[1])
    print({name + 's': set(pusty)})
print('**' * 30)

print('3. Użyj metody groupby do utworzenia słownika z liczbą wystąpień danej grupy w kolekcji.\n'
      ' Jak wyglądałby kod bez użycia tej metody? Zachowaj kod do późniejszego porównania, gdy poznamy z klasę Counter i Defaultdict.')
menu1 = sorted(menu1)
# print(menu1)
for name, group in groupby(menu1, lambda x: x[0]):
    nowe = []
    for i in group:
        nowe.append(i[1])
    print({name: len(set(nowe))})
