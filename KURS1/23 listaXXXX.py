'''
# 1
a=['w','r','o','c']
print(a[-1])
print(a[-1:1])
'''
'''#podaj napis i my wyświetlamy wszystkie znaki tekstu
tekst=input('Wpisz tekst: ')
for x in tekst:
    print(x)
    '''


'''#2 podaj napis i my wyświetlamy wystapieni litery
tekst=input('Wpisz tekst: ')
znak=input('policz ile jest znaku:')

counter=0
for x in tekst:
    if x==znak:
        counter+=1


print(counter)
'''
'''
#3suma cyfr
cyfra=input('Podaj cyfrę:')
suma=0

for znak in cyfra:
    suma=suma+int(znak)
print(suma)'''

'''
#4 lista o dowonym typie sumować elementy listy tylko liczby
lista=[1,False,'napis',2,3,7,True] #True zamieni na 1 bo (bool)
suma=0
for znak in lista:
    if isinstance(znak,int) and not isinstance(znak,bool): #sprawdzamy czy znak w liście jest int i nie bool
        suma=znak+suma

print(suma)
'''
#5 set
set={'a','s','d','f','a'} # unikalne elementy
print(set)
print(len(set))
