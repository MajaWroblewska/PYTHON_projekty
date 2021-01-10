# tuple operacje-indeksowanie od 0
# tuple=krotka
a=('a',[1,2,3],{4,5,6}, True,False)
print(a)
print('*'*30)
print(a[1]) # da się wypisać konktetną danej krotki
# a[0]=3 # nie da się zmienć danych w ktotce chyba ze elent w niej da sie zmodyfikować np. set i lista a nie 'str', bool
# a[3]=1
print('*'*30)
a[1][2]=5 #podmianka w 2el tuple do 3el listy w tuple
print(a)

a[2].add(7) # dodanie 7 w 2el tuple
print(a)



a=10
b=6
print('ab=',a,b)
print('ba=',b,a)