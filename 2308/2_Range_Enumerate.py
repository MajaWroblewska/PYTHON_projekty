
#1 wypisz liczby parzyste od 0-30
for i in range(0,30,2):
    print('Lp. parzysta: ',i)
print('*'*30)

#2 wypisz liczby nieparzyste od 0-30
for i in range(1,30,2):
    print('Lp. nieparzysta: ',i)
print('*'*30)

#3 wypisz liczby od 100-0 podzielne przez 4
for i in range(100,0,-1):
    if i % 4 == 0:
        print(i)
print('*'*30)

for x in range(100, 0, -4):
    print(x)
print('*'*30)

#4 od 1-10 co 2
for x in range(1,10,2): # range to nie lista
    print(x)
    print(range(5)) #wyswietli napis "range(0,5)"
print('*'*30)

#5 nic sie nie stanie bo range nie da sie oszukac bo jest krok -4
for x in range(1, 10, -4):
    print(x)
print('end')
print('*'*30)

#6 enumerate
lista={'a','b','c'}
for x in enumerate(lista): #enumerate wyświetli indeks i jej wartość
    print(x) #wyswietli jako tuplew nawiasach ()
    print(type(x))  # x to tuple
print('*'*30)

lista={'a','b','c'}
for x,y in enumerate(lista): #enumerate wyświetli indeks i jej wartość
    print(x,y)
print('*'*30)

#7 wypisanie w rzadku elementy listy
lista = ['1srt',{'2set'},3,True,[5,6],('tuple')]
for x in lista:
    print(x)
print('*'*30)

# lista = [6,2,3,6,5]
# for x in range(len()): #zle?????
#     print(lista[x])


