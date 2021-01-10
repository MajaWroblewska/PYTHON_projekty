'LAMBDA-Nnapisać funkcję, która z przekazanej listy słów zwróci listę zawierającą palindromy\
(niech wielkość liter nie ma znaczenia).'
# join łączy liste i str
# reversed odwraca kolejność listy

lista_slow=['Olo','zez', 'Ada', 'oko', 'kok', 'kajak', 'ara', 'Paweł', 'Iza','noc',"inni", "kajak", "raDar", "mama"]
print('lista_slow:',lista_slow)
print('ilość słów:',len(lista_slow))
print("---"*30)

fun1=map(lambda x : x.lower(), lista_slow)
print('fun1-lista_slow-małymi literami:',list(fun1))
print("---"*30)

fun2=map(lambda x : 'palindrom' if x.lower()==x.lower()[::-1] else 'nie', lista_slow)
print('fun2-info palindrom/nie:', list(fun2))
print("---"*30)

fun3=map(lambda x : x if x.lower()==x.lower()[::-1] else 'nie', lista_slow) #jak zrobić by nie wyświetlał słowa "NIE" i skrócił listę_slow
print('fun3-:', list(fun3))
print("---"*30)

# palindromy
result = list(filter(lambda x: (x.lower() == "".join(reversed(x.lower()))), lista_slow))
print('trener:', result)
print('trener ilość:', len(result))
print("---"*30)

x=['Maja', 'popi']
print('słowa',x)
a=map(lambda x: ''.join(reversed(x.lower())),x) #musi być join()
print('reversrd słów:', list(a))
print("---"*30)

########################################################################################
'lub tradycyjna pętla '

palindromy=[]

for i in lista_slow:
    slowo=i.lower()
    wspak=slowo[::-1]
    if slowo==wspak:
        palindromy.append(i)
print('lista palindromów-pętla:',palindromy)
print('ilość palindromów:', len(palindromy))

print("---"*30)




