'LAMBDA-Nnapisać funkcję, która z przekazanej listy słów zwróci listę zawierającą palindromy\
(niech wielkość liter nie ma znaczenia).'

lista_slow=['Olo','zez', 'Ada', 'oko', 'kok', 'kajak', 'ara', 'Paweł', 'Iza','noc']
print('lista_slow:',lista_slow)
print('ilość słów w liście:',len(lista_slow))
palindromy=[]


# for i in lista_slow:
#     slowo=i.lower()
#     wspak=slowo[::-1]
#     if slowo==wspak:
#         palindromy.append(i)
# print(palindromy)
# print('ilość palindromów:', len(palindromy))

fun1=map(lambda x : x.lower(), lista_slow)
print('fun1:',list(fun1))

fun2=map(lambda x : 'palindrom' if x.lower()==x.lower()[::-1] else 'nie', lista_slow)
print('fun2:', list(fun2))

fun3=map(lambda x : x if x.lower()==x.lower()[::-1] else 'nie', lista_slow)
print('fun3:', list(fun3))
# fun4=filter(list(fun3) : list(fun3)!='nie', lista_slow)
# print('fun4:', list(fun4))

# slowo='zez'
# wspak=slowo[::-1]
# print(wspak)

# if slowo==wspak:
#     print('TAK-palindrom')
# else:
#     print('NIE-palindrom')
