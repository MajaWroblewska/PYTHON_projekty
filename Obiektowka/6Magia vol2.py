class ListaUczniow(object):
    def __init__(self,lista):
        self.lista_uczniow=lista

    def __len__(self):
        return len(lista)

    def __add__(self, other):
        print(self)     # self to klasa_1a
        print(other)    # other to klasa_1b

        return self.lista_uczniow + other.lista_uczniow #????

lista=[1,2,3,4,5]
listaN=['la','9',5,7,8,7]

klasa_1a=ListaUczniow(lista)    # to self bo w print (linia 22) jest 1a+1b gdyby było 1b+1a to "lista"=other
klasa_1b=ListaUczniow(listaN)   # to other bo w print (linia 22) jest 1a+1b gdyby było 1b+1a to "listaN"=self

# klasa_1b + "klasa_1a"     # sumuje jak lista bo 1-szy składnik sumy to lista
# "klasa_1a" + klasa_1b     # sumuje jak string bo 1-szy składnik sumy to string
print(klasa_1a + klasa_1b)


lu=ListaUczniow(lista)  #init zada argumentu
# print(lu)           # obiekt lu
print(lu.__len__()) # wywołanie modułu __len__ w obiekcie lu
print(len(lu))      # długość obiektu lu - tak jak ma byś wyświetlany len na obiekcie klasy

