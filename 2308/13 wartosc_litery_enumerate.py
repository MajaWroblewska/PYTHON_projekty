import string


my_list = input('Podaj napis')
for i,x in enumerate(string.ascii_lowercase):
     print(i+1,x)

#print(type(ord('a')))
def wartosc_liter():
    for litera in my_list:
        value=ord(litera)-96
        if value<1 or value>26:
            value=0
            print(value)
        else:
            print(value)
    return value
wartosc_liter()

def zliczanie():
    for litera in my_list:
        print(wartosc_liter(my_list))

zliczanie()





        # lista_wartości=list(value)
        # print(lista_wartości)
    # twórz liste wartosci

    # for

# sumuj wartości


