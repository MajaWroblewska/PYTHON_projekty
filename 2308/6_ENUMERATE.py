lista=['a','b','c',['a','b','c'],8]
for i, x in enumerate(lista):
    print(i,x)
    print(x,i)  #zmiana kolejności
    print('typ i',type(i)) #typ int bo liczba
    print('typ x',type(x))    #typ str bo element listy to str (typ list bo element listy to lista itd)
print('*'*30)

for i in enumerate(lista):  #enumerate(lista)  # wyświetli tupla
    print(i)
print('*'*30)

for i in enumerate('lista'):  #enumerate(str)
    print(i)
print('*'*30)

