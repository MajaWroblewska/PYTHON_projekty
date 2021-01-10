'3. Dla dowolnego słownika zwróć listę stringów złączonymi za pomocą podkteślnika kluczami i wartościami,/' \
' gdzie klucz zostanie zamieniony na Wielką literę {"klucz":"wartość"} ->["Klucz_wartość"]'

print('Zad 3')
slownik = {'key1': '1', 'key2': '2', 'key3': 'None', 'klucz4': 'str'}
lista3 = []
print('lista3:', lista3)
print('slownik:', slownik)
print("---"*30)

filtr1 = list(map(lambda keys: (keys), slownik.keys()))
filtr2 = list(map(lambda values: (values), slownik.values()))

print('list_keys:',filtr1)
print("---"*30)

print('list_valu:',filtr2)
print("---"*30)

print('str list_keys= str(filtr1):', str(filtr1).title())
print("---"*30)

print('str list_values= str(filtr2):', str(filtr2))
print("---"*30)
#######################################################################################

print("print('_'.join(str(filtr1).title()+str(filtr2)))")
for i in filtr1:
    print('_'.join(str(filtr1).title()+str(filtr2)))

print("---"*30)

##########################################################################################
'rozwiązanie siłowe ale nie lista!!!!'
print('rozwiązanie siłowe ale nie lista!!!!')
print(filtr1[0].title()+'_'+filtr2[0])
print(filtr1[1].title()+'_'+filtr2[1])
print(filtr1[2].title()+'_'+filtr2[2])
print(filtr1[3].title()+'_'+filtr2[3])
print("---"*30)

##############################################################################################
print("for key, value in slownik.items():\
    print(key.title() + '_' + value, end=', ')")

for key, value in slownik.items():
    element=key.title() + '_' + value #->str
    print(element)
    print(type(element))
    list_element=list(element)  #->list
    print(list_element)
    print(type(list_element))

    print(key.title() + '_' + value, end=', ')  #->str


    print(type(key.title()))
    print('_'.join(str(key.title()+value)))

    print("***" * 30)

############################################################################



# print('*' * 30)

# x = ('key1', 'key2', 'key3')
# y = 0
# slo = dict.fromkeys(x, y)
# print(slo)



# for i in list(str(filtr1).title()):
#     print(i)
# nowa_lista=[]
