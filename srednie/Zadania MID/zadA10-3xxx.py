print('Zad 3')
slownik = {'key1': '1', 'key2': '2', 'key3': 'None', 'klucz4': 'str'}
lista3 = []
print('lista3:', lista3)
print('slownik:', slownik)
print("---"*30)

filtr1 = list(map(lambda keys: (keys), slownik.keys()))
filtr2 = list(map(lambda values: (values), slownik.values()))

list_dict=list(slownik.items())
print(list_dict)
print("---"*30)

# od Jany???
list_dict=list(slownik.items())
# d=
d1 = map(lambda x: f'{str(x[0]).upper()}_{x[1]}', slownik.items())
print(list(d1))
# print("---"*30)

print('siłowe rozwiązanie ale nie lista!!!!!!!!!!!')
print(list_dict[0][0].title()+'_'+ list_dict[0][1])
print(list_dict[1][0].title()+'_'+ list_dict[0][1])
print(list_dict[2][0].title()+'_'+ list_dict[0][1])
print(list_dict[3][0].title()+'_'+ list_dict[0][1])
print("---"*30)
#####################################################################################

map1=map(lambda x : '_'.join(x), list_dict)
print(list(map1))
print("---"*30)

lista=[]
for i in list_dict:
    for j in i:
        j=j.title()
        j=list(j)
        print(type(j))

        print(j)
        # print(j, end='_')   # Key1_1_Key2_2_Key3_None_Klucz4_Str_
# print(j)

# od Jany???
list_dict=list(slownik.items())
# d=
d1 = map(lambda x: f'{str(x[0]).title()}_{x[1]}', slownik.items())
print(list(d1))
# print("---"*30)